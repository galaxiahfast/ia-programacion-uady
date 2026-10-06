"""MCP Streamable HTTP server for the Amazon product search project."""

from functools import lru_cache
from pathlib import Path

from mcp.server import MCPServer
from mcp.server.mcpserver.exceptions import ToolError

from support.data import load_catalog
from support.encoder import SentenceEncoder
from support.models import ProductAnalysis, ProductComparison, SearchResult
from support.search import ProductSearch
from support.settings import load_settings

PROJECT_DIR = Path(__file__).resolve().parent
mcp = MCPServer("Amazon reviews")


@lru_cache(maxsize=1)
def get_search() -> ProductSearch:
    """Load data and embeddings once, on the first tool call."""
    settings = load_settings(PROJECT_DIR / "config.json")
    reviews, products = load_catalog(PROJECT_DIR / "datasets")
    encoder = SentenceEncoder(settings.model_name, settings.device)
    return ProductSearch(products, reviews, encoder, settings.batch_size)


@mcp.tool()
def search_products(query: str, top_k: int = 5) -> list[SearchResult]:
    """Find products related to an English query using semantic similarity."""
    try:
        return get_search().search_products(query, top_k)
    except ValueError as error:
        raise ToolError(str(error)) from error


@mcp.tool()
def analyze_product(product_id: str) -> ProductAnalysis:
    """Describe the selected ratings for one product."""
    try:
        return get_search().analyze_product(product_id)
    except ValueError as error:
        raise ToolError(str(error)) from error


@mcp.tool()
def compare_products(product_ids: list[str]) -> ProductComparison:
    """Compare rating summaries and means for distinct products."""
    try:
        return get_search().compare_products(product_ids)
    except ValueError as error:
        raise ToolError(str(error)) from error


if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="127.0.0.1", port=8000)
