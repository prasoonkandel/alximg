import base64
import os
from operator import ge
from tokenize import generate_tokens

import dotenv
import requests

dotenv.load_dotenv()

API_URL = os.getenv("OPENROUTER_API_URL")
API_KEY = os.getenv("OPENROUTER_API_KEY")

MODEL = "gemini-3.1-flash-image"
