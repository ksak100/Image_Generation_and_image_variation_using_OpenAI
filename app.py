from flask import Flask, render_template, request, redirect, url_for
from image_generation import ImageGeneration
from image_variation import ImageVariation
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'static/uploads'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/generate', methods=['GET', 'POST'])
def generate():
    image_url = None
    if request.method == 'POST':
        prompt = request.form['prompt']
        quality = request.form['quality']
        img_generate=ImageGeneration(prompt, quality)
        image_url = img_generate.generate_image()
    return render_template('generate.html', image_url=image_url)

@app.route('/variation', methods=['GET', 'POST'])
def variation():
    image_url = None
    if request.method == 'POST':
        if 'image' not in request.files:
            return redirect(request.url)
        file = request.files['image']
        if file.filename == '':
            return redirect(request.url)
        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            img_variation=ImageVariation(file_path)
            image_url = img_variation.image_variation()
    return render_template('variation.html', image_url=image_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
