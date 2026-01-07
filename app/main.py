from fastapi import FastAPI
from app.core.bootstrap import create_app

app: FastAPI = create_app()
