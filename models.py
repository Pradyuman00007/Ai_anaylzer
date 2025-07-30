from pydantic import BaseModel

class SectorAnalysisRequest(BaseModel):
    sector: str
