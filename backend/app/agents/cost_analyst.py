"""
Node 5 — The COST ANALYST (Financial)
"No-surprises" auditor: scrapes true cost and compares to Snowflake history.

Scraping Strategy:
  1. Firecrawl /map  → discover "Pricing" / "Menu" page on venue website
  2. Jina Reader      → fetch "General Info" pages (free, zero-config fallback)
  3. Firecrawl /scrape → extract structured pricing via Pydantic schema

Tools: Firecrawl, Jina Reader
"""

import httpx

from app.models.state import PathfinderState
from app.core.config import settings

# Jina Reader base URL — prepend to any URL for clean markdown extraction
JINA_READER_BASE = "https://r.jina.ai/"


async def _jina_read(url: str) -> str:
    """Fetch a URL through Jina Reader and return clean markdown."""
    async with httpx.AsyncClient(timeout=15) as client:
        resp = await client.get(f"{JINA_READER_BASE}{url}")
        resp.raise_for_status()
        return resp.text


async def _firecrawl_map(website_url: str) -> list:
    """Use Firecrawl /map to discover sub-pages (e.g. Pricing, Menu)."""
    # TODO: call Firecrawl /map endpoint with FIRECRAWL_API_KEY
    # Returns list of discovered page URLs
    return []


async def _firecrawl_scrape(page_url: str, schema: dict) -> dict:
    """Use Firecrawl /scrape to extract structured data via a Pydantic schema."""
    # TODO: call Firecrawl /scrape endpoint with extract schema
    # Returns typed pricing data matching the schema
    return {}


def cost_analyst_node(state: PathfinderState) -> PathfinderState:
    """
    Compute Total Cost of Attendance (TCA) per venue.

    Steps
    -----
    1. For each venue, use Firecrawl /map to find the pricing / menu page.
    2. Use Jina Reader to fetch general info pages (fallback / supplementary).
    3. Use Firecrawl /scrape with a Pydantic schema to extract structured pricing.
    4. Compute TCA: base cost + hidden fees + equipment + min spends.
    5. Query Snowflake Cortex for historical price baselines.
    6. Flag seasonal spikes or misleading discounts.
    7. Return updated state with cost_profiles.
    """
    # TODO: implement full scraping pipeline + Snowflake comparison
    return state
