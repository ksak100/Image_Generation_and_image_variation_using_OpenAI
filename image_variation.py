import openai
from openai import OpenAI
import sys
from src.utils import get_image_file_path

class ImageVariation():
    def __init__(self,file_path):
        self.filepath, self.mode=file_path, 'rb'

    def image_variation(self):

        try:
            client=OpenAI()

            response=client.images.create_variation(
                model='dall-e-2',
                image=open(self.filepath, self.mode),
                n=1,
                size='1024x1024'
            )

            image_url=response.data[0].url
            return image_url
        except Exception as e:
            print(e)

if __name__=='__main__':
    img_variation = ImageVariation()
    image_url=img_variation.image_variation()
    print(image_url)