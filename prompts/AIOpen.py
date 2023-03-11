import os
import openai
from dotenv import load_dotenv

from fastapi import Depends

load_dotenv()

# import requests
from PIL import Image
import sys
sys.path.append(sys.path[0] + "/..")
from model.model import Descriptions


from fastapi.responses import JSONResponse 

class ImageGenerator:
    def __init__(self) -> str:
        self.image_url: str
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.APIKey = openai.api_key
        self.name = None

    def generateImage(self, description: Descriptions):
       
       try:        
        self.APIKey
        response = openai.Image.create(
            prompt = description.prompt,
            n = description.n,
            size= description.Squaresize,
            )
        
        self.image_url = response['data']

        self.image_url = [image["url"] for image in self.image_url]
        
        return JSONResponse(status_code=200, content={"URL": self.image_url, "message": "Success"})
       except:
          return JSONResponse(status_code=500, content={"message":"Error generating images"})
          
          
          
    
    # def downloadImage(self, names)-> None:
    #   try:
    #     self.name = names
    #     for url in self.image_url:
    #       image = requests.get(url)
    #     for name in self.name:
    #         with open("{}.png".format(name), "wb") as f:
    #           f.write(image.content)
    #   except:
    #      print("An error occured")
    #   return self.name
    
    # def convertImage(self, imageName, RGBAName)->str:
    #    image = Image.open("{}.png".format(imageName))
    #    rgba_image = image.convert('RGBA')
    #    rgba_image.save("{}.png".format(RGBAName))

    #    return RGBAName
    
    # def editImage(self, imageName, maskName) -> str:
    #   self.convertImage("IdowuPaul2", maskName)
       
    #   response = openai.Image.create_edit(
    #       image=open("{}.png".format(imageName), "rb"),
    #       mask=open("{}.png".format(maskName), "rb"),
    #       prompt="A sunlit indoor lounge area with a pool containing a flamingo",
    #       n=1,
    #       size="1024x1024"
    #       )

       
    
        
    




