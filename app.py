from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pydantic.types import Json
from pydantic_core.core_schema import ErrorType

from services.imgen import generate_image
from services.prompt import generate_prompt
from test.test import image_url

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Image(BaseModel):
    theme_id: int
    input_image_url: str


@app.get("/")
def root():
    return {"message": "Welcome to Alximg"}, 200
