from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Soft fotbal online ✅"}
