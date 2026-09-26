import base64
import io
import os

import dotenv
import requests

dotenv.load_dotenv()

API_URL = os.getenv("OPENROUTER_API_URL")
API_KEY = os.getenv("OPENROUTER_API_KEY")

MODEL = "gemini-3.1-flash-image"


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
        "image_config": {"aspect_ratio": "4:3"},
    }
    response = requests.post(API_URL, headers=headers, json=data)
    response.raise_for_status()
    result = response.json()
    message = result["choices"][0]["message"]

    if "images" not in message:
        text_content = message.get("content", "No content returned.")
        raise ValueError(
            f"Model failed to generate an image. API returned text instead:\n{text_content}"
        )

    image_data = message["images"][0]["image_url"]["url"]

    if "," in image_data:
        base64_data = image_data.split(",", 1)[1]
    else:
        base64_data = image_data
        image_bytes = base64.b64decode(base64_data)
        return io.BytesIO(image_bytes)

    image_bytes = base64.b64decode(base64_data)
    return io.BytesIO(image_bytes)
