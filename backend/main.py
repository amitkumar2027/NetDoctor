from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="NetDoctor API",
    description="Backend API for Internet fault diagnosis",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "NetDoctor API is running",
        "version": "0.1.0",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/diagnosis/start")
def start_diagnosis():
    # The Python agent will be connected here in the next phase.
    return {
        "status": "started",
        "message": "Diagnosis workflow will run here.",
    }
