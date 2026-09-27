import os

import numpy as np
import requests
from dotenv import load_dotenv
from services.vector import normalise_vector

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
API_URL = os.getenv("OPENROUTER_API_URL")

embedding_model = "voyage-4-lite"

DIMENSIONS = 1024


def normalise_embedding_vectors(vector):
    return vector / np.linalg.norm(vector)
