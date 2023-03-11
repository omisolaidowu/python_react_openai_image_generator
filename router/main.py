import sys
sys.path.append(sys.path[0] + "/..")

from prompts.AIOpen import ImageGenerator

from fastapi import FastAPI, APIRouter

from fastapi.middleware.cors import CORSMiddleware

from dotenv import load_dotenv

load_dotenv()
import os

import uvicorn

imageGen = ImageGenerator()

origins = [
    "http://localhost:8080",
]



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials= True,
    allow_methods = ["*"],
    allow_headers = ["*"],
   
)


router = APIRouter()

router.add_api_route('/api/generateimage', 
endpoint = imageGen.generateImage, methods=["POST"])


app.include_router(router)


if __name__ == "__main__":
   uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)