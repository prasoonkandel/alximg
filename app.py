from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pydantic.types import Json
from pydantic_core.core_schema import ErrorType

from services.imgen import generate_image
from services.json import get_all_themes
from services.prompt import generate_prompt

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


@app.post("/generate-image")
def send_image(image_req: Image):
    try:
        prompt = generate_prompt(image_req.theme_id)
        output_image_url = generate_image(prompt, image_req.input_image_url)
        return {"message": "Image Generated Succesfully", "image_url": output_image_url}
    except Exception as e:
        return {"error": e}


@app.get("/get-all-themes")
def send_all_themes():
    try:
        all_themes = get_all_themes()
        return {"message": "All themes Fetched", "themes": all_themes}
    except Exception as e:
        return {"error": e}
