from PIL import Image

# Get users prompt for image generation
def user_prompt():
    prompt=str(input("Please enter the description of image you want: \n"))
    return prompt

# Get the quality of image user wants 
def user_quality():
    quality=str(input("Select the quality of image you want: 'standard' or 'hd' \n"))
    return quality

# Check if the image given is in png format or not for further processing
def is_png(image_path):
    try:
        with Image.open(image_path) as img:
            if img.format != 'PNG':
                return True
            else: False
    except Exception as e:
        print(e)


# Get image file path
def get_image_file_path():
    try:
        img_path = str(input("Please Enter file path of the image you want a variation. \n"))
        if is_png(img_path):
           raise ValueError("The file is not a PNG format image.")
        else:
            return img_path, "rb"
    except ValueError as e:
        print(e)

    
