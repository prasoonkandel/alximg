from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pydantic.types import Json
from pydantic_core.core_schema import ErrorType

from services.imgen import generate_image
from services.prompt import generate_prompt
