import base64
import io
import os

import dotenv
import requests

dotenv.load_dotenv()

API_URL = os.getenv("OPENROUTER_API_URL")
API_KEY = os.getenv("OPENROUTER_API_KEY")

MODEL = "google/gemini-3.1-flash-image"


def generate_image(prompt, input_image_url):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "OpenAI-Compatibility": "true",
        "Content-Type": "application/json",
    }
    data = {
        "model": MODEL,
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": input_image_url}},
                ],
            }
        ],
        "modalities": ["image", "text"],
        "image_config": {"aspect_ratio": "3:4"},
    }
    response = requests.post(API_URL, headers=headers, json=data)
    response.raise_for_status()
    result = response.json()
    message = result["choices"][0]["message"]

    if "images" not in message or not message["images"]:
        raise ValueError(f"No image returned by the model.")

    output_image_url = message["images"][0]["image_url"]["url"]

    return output_image_url
