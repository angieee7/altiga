from fastapi import FastAPI
from src.ghg_calculator import GHGCalculator

app = FastAPI(title="Altiga GHG Calculator API")

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Altiga GHG Calculator is running"}
