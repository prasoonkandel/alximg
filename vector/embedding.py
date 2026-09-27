import os

import numpy as np
import requests
from dotenv import load_dotenv

from vector.operations import normalise_vector

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
API_URL = os.getenv("OPENROUTER_EMBEDDING_API_URL")

embedding_model = "voyage-4-lite"

DIMENSIONS = 1024


def get_embedding(text):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {"model": embedding_model, "input": text, "dimensions": DIMENSIONS}

    response = requests.post(API_URL, headers=headers, json=payload)

    response.raise_for_status()

    data = response.json()

    return normalise_vector(np.array(data["data"][0]["embedding"], dtype=np.float32))
