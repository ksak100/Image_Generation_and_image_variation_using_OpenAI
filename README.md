# Image Generation and Image Variation

This project demonstrates a web application built with Flask to generate images based on text prompts and create variations of existing images using the OpenAI API.

## Project Structure

- `app.py`: The main Flask application file that handles the web server and routes.
- `image_variation.py`: Contains the logic to generate variations of an existing image using OpenAI's DALL-E model.
- `image_generation.py`: Contains the logic to generate image from users prompt using OpenAI's DALL-E model
- `utils.py`: Utility functions for image handling and user prompts.
- `setup.py`: Function to install required packages
- 

## Features

1. **Image Generation**: Generate images based on user-provided text prompts.
2. **Image Variation**: Upload an image to create variations of it.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/ksak100/Image_Generation_and_image_variation_using_OpenAI.git
   cd Image_Generation_and_image_variation_using_OpenAI
   ```

2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

4. Set up your OpenAI API key in your environment:
   ```sh
   export OPENAI_API_KEY='your-api-key-here'
   ```
   On Windows
    ```sh
   set OPENAI_API_KEY='your-api-key-here'
   ```

## Usage

1. Run the Flask application:
   ```sh
   python app.py
   ```

2. Open your web browser and navigate to `http://localhost:5000` to access the application.

## Routes

- `/`: Home page.
- `/generate`: Page for generating images based on text prompts.
- `/variation`: Page for uploading an image and generating its variations.

## File Descriptions

### `app.py`

This file sets up the Flask application with three routes:
- `/`: Renders the home page.
- `/generate`: Handles the form submission for image generation based on text prompts.
- `/variation`: Handles the image upload and generates variations using the provided image.

### `utils.py`

This file contains utility functions:
- `user_prompt()`: Prompts the user for a description of the image to be generated.
- `user_quality()`: Prompts the user to select the quality of the image (standard or HD).
- `is_png(image_path)`: Checks if the provided image path is a PNG format.
- `get_image_file_path()`: Prompts the user for the image file path and verifies if it's a PNG.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries, please contact [kunalsingh974@gmail.com].

## app.py on localhost 127.0.0.1:5000 

Home page
![image](https://github.com/user-attachments/assets/0f4c51fd-1bb1-44da-a210-aea1d500a33d)

Generate Image
![image](https://github.com/user-attachments/assets/3add2bd3-3536-44ae-9e10-297ef755741c)

Image Variation
![image](https://github.com/user-attachments/assets/49380b9f-953f-4f38-ba48-dd2a189b2151)






