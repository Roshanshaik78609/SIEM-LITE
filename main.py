from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "project": "SIEM-Lite",
        "status": "running"
    }