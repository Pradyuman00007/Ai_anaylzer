import httpx

async def fetch_sector_data(sector: str) -> str:
    query = f"Latest market news in {sector} sector in India"
    url = f"https://api.duckduckgo.com/?q={query}&format=json"
    
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        data = resp.json()
        return data.get("AbstractText") or f"No data found for {sector}."
