import logging
import os

from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware
from gpt4all import GPT4All
from api_v1 import events
from api_v1.api import router as v1_router

from settings import settings


logger = logging.getLogger(__name__)
app = FastAPI(title='GPT4All API', description="API for GPT4All following OpenAI specifications", version="0.0.1")

# CORS Configuration (in-case you want to deploy)
app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["GET", "POST", "OPTIONS"],
  allow_headers=["*"],
)

# API Endpoints
logger.info('Adding v1 endpoints..')
app.include_router(v1_router, prefix='/v1')
app.add_exception_handler(HTTPException, events.on_http_error)

# Event handlers
@app.on_event("startup")
async def startup():
  logger.info(f"Downloading/fetching model at {os.path.join(settings.gpt4all_path, settings.model)}")

  # Download or fetch model
  GPT4All(model_name=settings.model, model_path=settings.gpt4all_path)

  logger.info(f"GPT4All API is ready to infer from {settings.model}, waiting for requests..")

@app.on_event("shutdown")
async def shutdown():
  logger.info("Shutting down API")


# https://github.com/tiangolo/fastapi/issues/2019
LOG_FORMAT2 = (
  "[%(asctime)s %(process)d:%(threadName)s] %(name)s - %(levelname)s - %(message)s |  %(filename)s:%(lineno)d"
)
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT2)
