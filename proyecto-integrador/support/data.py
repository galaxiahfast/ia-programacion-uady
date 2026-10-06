"""Load the provided compressed Amazon review selection."""

import gzip
import json
from collections.abc import Iterator
from pathlib import Path
from typing import cast

from support.models import ProductRecord, ReviewRecord


def _rows(path: Path) -> Iterator[tuple[int, dict[str, object]]]:
    if not path.is_file():
        raise FileNotFoundError(f"Missing dataset file: {path}")
    with gzip.open(path, "rt", encoding="utf-8") as stream:
        for line_number, text in enumerate(stream, start=1):
            if not text.strip():
                continue
            raw = cast(object, json.loads(text))
            if not isinstance(raw, dict):
                raise ValueError(f"Expected an object at {path.name}:{line_number}")
            yield line_number, cast(dict[str, object], raw)


def _string_list(value: object, field: str, line_number: int) -> list[str]:
    if value is None:
        return []
    if not isinstance(value, list) or any(not isinstance(item, str) for item in value):
        raise ValueError(f"Invalid {field} at product line {line_number}")
    return [item for item in value if isinstance(item, str)]


def load_catalog(
    directory: Path,
) -> tuple[list[ReviewRecord], dict[str, ProductRecord]]:
    """Read products and reviews while preserving their file order."""
    products: dict[str, ProductRecord] = {}
    for line_number, row in _rows(directory / "products.jsonl.gz"):
        product_id = row.get("parent_asin")
        title = row.get("title")
        family = row.get("family")
        if not isinstance(product_id, str) or not product_id.strip():
            raise ValueError(f"Invalid product ID at product line {line_number}")
        if not isinstance(title, str) or not title.strip():
            raise ValueError(f"Invalid title at product line {line_number}")
        if not isinstance(family, str) or not family.strip():
            raise ValueError(f"Invalid family at product line {line_number}")
        if product_id in products:
            raise ValueError(f"Duplicate product ID at product line {line_number}")
        products[product_id] = {
            "product_id": product_id,
            "title": title,
            "features": _string_list(row.get("features"), "features", line_number),
            "description": _string_list(
                row.get("description"), "description", line_number
            ),
            "categories": _string_list(
                row.get("categories"), "categories", line_number
            ),
            "family": family,
        }

    reviews: list[ReviewRecord] = []
    review_ids: set[str] = set()
    for line_number, row in _rows(directory / "reviews.jsonl.gz"):
        product_id = row.get("parent_asin")
        rating = row.get("rating")
        text = row.get("text")
        source_line = row.get("source_line")
        if not isinstance(product_id, str) or product_id not in products:
            raise ValueError(f"Unknown product at review line {line_number}")
        if (
            isinstance(rating, bool)
            or not isinstance(rating, (int, float))
            or rating not in (1, 2, 3, 4, 5)
        ):
            raise ValueError(f"Invalid rating at review line {line_number}")
        if not isinstance(text, str) or not text.strip():
            raise ValueError(f"Invalid text at review line {line_number}")
        if (
            isinstance(source_line, bool)
            or not isinstance(source_line, int)
            or source_line < 1
        ):
            raise ValueError(f"Invalid source line at review line {line_number}")
        review_id = f"Electronics:{source_line}"
        if review_id in review_ids:
            raise ValueError(f"Duplicate review ID at review line {line_number}")
        review_ids.add(review_id)
        reviews.append(
            {
                "review_id": review_id,
                "product_id": product_id,
                "text": text.strip(),
                "rating": float(rating),
            }
        )

    if not products or not reviews:
        raise ValueError("The product and review files must not be empty")
    return reviews, products
