"""Vector search and descriptive review statistics."""

from collections import defaultdict
from collections.abc import Sequence

import numpy as np
import numpy.typing as npt

from support.encoder import FloatMatrix, TextEncoder
from support.models import (
    ProductAnalysis,
    ProductComparison,
    ProductRecord,
    ReviewRecord,
    SearchResult,
)


def _normalize(vector: npt.NDArray[np.float32]) -> npt.NDArray[np.float32]:
    length = float(np.linalg.norm(vector))
    if length == 0.0:
        raise ValueError("Cannot normalize a zero vector")
    return np.asarray(vector / length, dtype=np.float32)


class ProductSearch:
    """Prepare reusable product vectors and answer all three operations."""

    def __init__(
        self,
        products: dict[str, ProductRecord],
        reviews: Sequence[ReviewRecord],
        encoder: TextEncoder,
        batch_size: int,
    ) -> None:
        if not products or not reviews:
            raise ValueError("Products and reviews must not be empty")
        if batch_size <= 0:
            raise ValueError("batch_size must be positive")
        self._products = products
        self._encoder = encoder
        self._batch_size = batch_size
        self._product_ids = list(products)
        self._reviews_by_product: dict[str, list[ReviewRecord]] = defaultdict(list)
        for review in reviews:
            if review["product_id"] not in products:
                raise ValueError(f"Unknown review product: {review['product_id']}")
            self._reviews_by_product[review["product_id"]].append(review)
        self._vectors = self._prepare_vectors()

    def _prepare_vectors(self) -> FloatMatrix:
        catalog_texts = [
            " ".join(
                [
                    self._products[product_id]["title"],
                    *self._products[product_id]["features"],
                    *self._products[product_id]["description"],
                ]
            ).strip()
            for product_id in self._product_ids
        ]
        catalog_vectors = self._encoder.encode(catalog_texts, self._batch_size)

        review_texts: list[str] = []
        review_product_ids: list[str] = []
        for product_id in self._product_ids:
            for review in self._reviews_by_product[product_id]:
                review_texts.append(review["text"])
                review_product_ids.append(product_id)
        review_vectors = self._encoder.encode(review_texts, self._batch_size)

        positions: dict[str, list[int]] = defaultdict(list)
        for index, product_id in enumerate(review_product_ids):
            positions[product_id].append(index)

        combined: list[npt.NDArray[np.float32]] = []
        for index, product_id in enumerate(self._product_ids):
            product_positions = positions[product_id]
            if not product_positions:
                review_summary = catalog_vectors[index]
            else:
                review_average = review_vectors[product_positions].mean(axis=0)
                review_summary = _normalize(review_average)
            combined.append(
                _normalize(0.5 * catalog_vectors[index] + 0.5 * review_summary)
            )
        matrix = np.stack(combined).astype(np.float32, copy=False)
        if matrix.shape[0] != len(self._product_ids):
            raise ValueError("Product vectors lost their correspondence with IDs")
        return matrix

    def search_products(self, query: str, top_k: int = 5) -> list[SearchResult]:
        if not query.strip():
            raise ValueError("query must not be empty")
        if (
            isinstance(top_k, bool)
            or not isinstance(top_k, int)
            or not 1 <= top_k <= 20
        ):
            raise ValueError("top_k must be an integer between 1 and 20")
        query_vector = self._encoder.encode([query.strip()], self._batch_size)[0]
        scores = self._vectors @ query_vector
        limit = min(top_k, len(self._product_ids))
        order = np.argsort(-scores, kind="stable")[:limit]
        return [
            {
                "product_id": self._product_ids[int(index)],
                "title": self._products[self._product_ids[int(index)]]["title"],
                "similarity": float(scores[int(index)]),
                "review_count": len(
                    self._reviews_by_product[self._product_ids[int(index)]]
                ),
            }
            for index in order
        ]

    def analyze_product(self, product_id: str) -> ProductAnalysis:
        clean_id = product_id.strip()
        if not clean_id:
            raise ValueError("product_id must not be empty")
        product = self._products.get(clean_id)
        selected = self._reviews_by_product.get(clean_id, [])
        counts = {str(star): 0 for star in range(1, 6)}
        for review in selected:
            counts[str(int(review["rating"]))] += 1
        total = len(selected)
        proportions = {
            star: (count / total if total else 0.0) for star, count in counts.items()
        }
        ratings = np.asarray(
            [review["rating"] for review in selected], dtype=np.float64
        )
        return {
            "product_id": clean_id,
            "title": product["title"] if product is not None else None,
            "review_count": total,
            "rating_counts": counts,
            "rating_proportions": proportions,
            "mean": float(ratings.mean()) if total else None,
            "median": float(np.median(ratings)) if total else None,
        }

    def compare_products(self, product_ids: Sequence[str]) -> ProductComparison:
        if len(product_ids) < 2:
            raise ValueError("At least two product IDs are required")
        cleaned = [product_id.strip() for product_id in product_ids]
        if any(not product_id for product_id in cleaned):
            raise ValueError("product IDs must not be empty")
        if len(set(cleaned)) != len(cleaned):
            raise ValueError("product IDs must be distinct")
        analyses = [self.analyze_product(product_id) for product_id in cleaned]
        reference = analyses[0]["mean"]
        differences: dict[str, float | None] = {}
        for analysis in analyses:
            current = analysis["mean"]
            differences[analysis["product_id"]] = (
                current - reference
                if current is not None and reference is not None
                else None
            )
        return {
            "products": analyses,
            "mean_differences_from_first": differences,
        }
