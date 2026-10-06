"""Shared data structures used by the project."""

from typing import TypedDict


class ProductRecord(TypedDict):
    product_id: str
    title: str
    features: list[str]
    description: list[str]
    categories: list[str]
    family: str


class ReviewRecord(TypedDict):
    review_id: str
    product_id: str
    text: str
    rating: float


class SearchResult(TypedDict):
    product_id: str
    title: str
    similarity: float
    review_count: int


class ProductAnalysis(TypedDict):
    product_id: str
    title: str | None
    review_count: int
    rating_counts: dict[str, int]
    rating_proportions: dict[str, float]
    mean: float | None
    median: float | None


class ProductComparison(TypedDict):
    products: list[ProductAnalysis]
    mean_differences_from_first: dict[str, float | None]
