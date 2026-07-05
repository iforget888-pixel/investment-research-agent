from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import get_settings
from app.db import Base, engine
from app.routers import health, raw_materials, watchlist

settings = get_settings()

app = FastAPI(title="Investment Research Agent API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origin_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def create_tables() -> None:
    Base.metadata.create_all(bind=engine)


app.include_router(health.router)
app.include_router(watchlist.router, prefix="/watchlist", tags=["watchlist"])
app.include_router(raw_materials.router, prefix="/raw-materials", tags=["raw-materials"])
