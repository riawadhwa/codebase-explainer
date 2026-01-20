from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from app.api.analyze import router as analyze_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Codebase Explainer Agent")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # fine for demo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(analyze_router)

@app.get("/")
def health_check():
    return {"status": "ok"}
