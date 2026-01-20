from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
import os
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.api.analyze import router as analyze_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Codebase Explainer Agent")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, "..", "frontend", "dist")

app.mount(
    "/assets",
    StaticFiles(directory=os.path.join(FRONTEND_DIR, "assets")),
    name="assets",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # fine for demo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analyze_router)

@app.get("/")
def serve_frontend():
    return FileResponse(os.path.join(FRONTEND_DIR, "index.html"))
