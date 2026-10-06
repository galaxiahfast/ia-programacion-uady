"""Tests for data validation, vector search and rating summaries."""

import json
from collections.abc import Callable, Sequence
from pathlib import Path

import numpy as np
import pytest

from support.data import load_catalog
from support.encoder import FloatMatrix
from support.models import ProductRecord, ReviewRecord
from support.search import ProductSearch
from support.settings import load_settings

PROJECT_DIR = Path(__file__).resolve().parents[1]


class MappingEncoder:
    def __init__(self, vectors: dict[str, list[float]]) -> None:
        self._vectors = vectors

    def encode(self, texts: Sequence[str], batch_size: int) -> FloatMatrix:
        assert batch_size > 0
        matrix = np.asarray([self._vectors[text] for text in texts], dtype=np.float32)
        lengths = np.linalg.norm(matrix, axis=1, keepdims=True)
        return np.asarray(matrix / lengths, dtype=np.float32)


@pytest.fixture
def sample_search() -> ProductSearch:
    products: dict[str, ProductRecord] = {
        "P1": {
            "product_id": "P1",
            "title": "Speaker",
            "features": [],
            "description": [],
            "categories": ["Audio"],
            "family": "Audio",
        },
        "P2": {
            "product_id": "P2",
            "title": "Headphones",
            "features": [],
            "description": [],
            "categories": ["Audio"],
            "family": "Audio",
        },
    }
    reviews: list[ReviewRecord] = [
        {"review_id": "R1", "product_id": "P1", "text": "clear", "rating": 5.0},
        {"review_id": "R2", "product_id": "P1", "text": "loud", "rating": 3.0},
        {"review_id": "R3", "product_id": "P2", "text": "soft", "rating": 1.0},
    ]
    vectors = {
        "Speaker": [1.0, 0.0],
        "Headphones": [0.0, 1.0],
        "clear": [0.0, 1.0],
        "loud": [0.0, 1.0],
        "soft": [0.0, 1.0],
        "portable": [1.0, 0.0],
    }
    return ProductSearch(products, reviews, MappingEncoder(vectors), batch_size=2)


def test_provided_dataset_and_settings_are_complete() -> None:
    reviews, products = load_catalog(PROJECT_DIR / "datasets")
    settings = load_settings(PROJECT_DIR / "config.json")
    assert len(products) == 600
    assert len(reviews) == 6992
    assert set(review["product_id"] for review in reviews) == set(products)
    assert settings.model_name == "sentence-transformers/all-MiniLM-L6-v2"
    assert settings.batch_size == 32


def test_search_uses_combined_normalized_vectors(sample_search: ProductSearch) -> None:
    results = sample_search.search_products("portable", top_k=2)
    assert [result["product_id"] for result in results] == ["P1", "P2"]
    assert results[0]["similarity"] == pytest.approx(2**-0.5)
    assert results[0]["review_count"] == 2
    assert results[0]["similarity"] >= results[1]["similarity"]


def test_analysis_includes_all_stars_and_unknown_product(
    sample_search: ProductSearch,
) -> None:
    analysis = sample_search.analyze_product("P1")
    assert analysis["review_count"] == 2
    assert analysis["rating_counts"] == {"1": 0, "2": 0, "3": 1, "4": 0, "5": 1}
    assert analysis["rating_proportions"] == {
        "1": 0.0,
        "2": 0.0,
        "3": 0.5,
        "4": 0.0,
        "5": 0.5,
    }
    assert analysis["mean"] == 4.0
    assert analysis["median"] == 4.0

    unknown = sample_search.analyze_product("UNKNOWN")
    assert unknown["review_count"] == 0
    assert unknown["mean"] is None
    assert unknown["median"] is None
    assert sum(unknown["rating_proportions"].values()) == 0.0


def test_comparison_is_relative_to_first_product(sample_search: ProductSearch) -> None:
    comparison = sample_search.compare_products(["P1", "P2", "UNKNOWN"])
    assert comparison["mean_differences_from_first"] == {
        "P1": 0.0,
        "P2": -3.0,
        "UNKNOWN": None,
    }


@pytest.mark.parametrize(
    ("operation", "message"),
    [
        (lambda search: search.search_products("", 5), "query"),
        (lambda search: search.search_products("portable", 0), "top_k"),
        (lambda search: search.search_products("portable", 21), "top_k"),
        (lambda search: search.analyze_product("  "), "product_id"),
        (lambda search: search.compare_products(["P1"]), "two product"),
        (lambda search: search.compare_products(["P1", "P1"]), "distinct"),
    ],
)
def test_invalid_calls_do_not_damage_following_calls(
    sample_search: ProductSearch,
    operation: Callable[[ProductSearch], object],
    message: str,
) -> None:
    with pytest.raises(ValueError, match=message):
        operation(sample_search)
    assert sample_search.search_products("portable", 1)[0]["product_id"] == "P1"


def test_invalid_configuration_is_rejected(tmp_path: Path) -> None:
    path = tmp_path / "config.json"
    path.write_text(
        json.dumps({"model_name": "", "batch_size": 0, "device": "cpu"}),
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="model_name"):
        load_settings(path)
