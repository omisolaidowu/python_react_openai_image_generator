from pydantic import BaseModel

from fastapi import Form

from dataclasses import dataclass



@dataclass
class Descriptions():
    prompt: str = Form(...)
    n: int = Form(...)
    Squaresize: str = Form(...)