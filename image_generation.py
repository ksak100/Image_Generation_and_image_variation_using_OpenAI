import openai
from openai import OpenAI
import sys
import os
from src.logger import logging
from src.exception import CustomException
from src.utils import user_prompt
from src.utils import user_quality

class ImageGeneration():
    def __init__(self, prompt, quality):

        self.prompt=prompt
        self.quality=quality
    
    def generate_image(self):
        logging.info("Starting generating images using given prompt")

        try:
            client=OpenAI()
            response = client.images.generate(
                model="dall-e-3",
                prompt=self.prompt,
                size='1024x1024',
                quality=self.quality,
                n=1
            )

            image_url=response.data[0].url

            logging.info("Completed Generating image")
            return image_url

        except openai.OpenAIError as e:
            print(e)

if __name__=='__main__':
    img_generation = ImageGeneration()
    image_url=img_generation.generate_image()
    print(image_url)