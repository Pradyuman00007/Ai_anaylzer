from fastapi import FastAPI, Depends, HTTPException, Request
from slowapi.middleware import SlowAPIMiddleware
from app.dependencies import limiter, authenticate
from app.collector import fetch_sector_data
from app.ai_analysis import analyze_with_gemini
from app.markdown_reporter import save_markdown_report
from app.storage import store_analysis  # ✅ Import storage function

app = FastAPI(title="Trade Opportunities API")
app.add_middleware(SlowAPIMiddleware)
app.state.limiter = limiter

@app.get("/analyze/{sector}", dependencies=[Depends(authenticate)])
@limiter.limit("5/minute")
async def analyze_sector(request: Request, sector: str):  # ✅ request required for rate limiter
    try:
        raw_data = await fetch_sector_data(sector)
        analysis = await analyze_with_gemini(sector, raw_data)
        filename = save_markdown_report(sector, analysis)

        # ✅ Store in storage (in-memory)
        store_analysis(sector, raw_data, analysis, filename)

        return {
            "status": "success",
            "sector": sector,
            "report_file": filename,
            "markdown_report": analysis
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
