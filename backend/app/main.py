from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from app.core.config import settings
from app.db.base import Base
from app.db.session import engine
from app.db import models
from app.api.routes import router
from app.seed import seed

@asynccontextmanager
async def lifespan(app: FastAPI):
    seed()
    from app.agents.support_workflow.checkpointer import initialize_checkpointer, close_checkpointer
    await initialize_checkpointer()
    yield
    await close_checkpointer()

app=FastAPI(title="SupportPilot AI",version="1.0.0",description="AI-assisted customer support workspace",lifespan=lifespan)
app.add_middleware(CORSMiddleware,allow_origins=settings.cors_origin_list,allow_credentials=True,allow_methods=["*"],allow_headers=["*"],)
app.include_router(router)

@app.get("/health",tags=["Health"])
def health():
    return {"status":"ok","service":"SupportPilot AI"}

@app.get("/ready",tags=["Health"])
def ready():
    try:
        with engine.connect() as connection: connection.execute(text("SELECT 1"))
        return {"status":"ready","database":"connected"}
    except Exception as exc:
        raise HTTPException(status_code=503, detail="Database unavailable") from exc
