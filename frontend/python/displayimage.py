import os
from flask import Flask, jsonify

imageFolder = os.path.join(os.getcwd(), 'images')

app = Flask(__name__)
@app.route("/gallery")
def getImages():
    imageFiles = os.listdir(imageFolder)
    images = []
    for file in imageFiles:
        if file.lower().endswith('.png'):
            images.append(file)
    images = jsonify(images)
    return images

def galleryPage():

    return render_templates('gallery.html', image_id = image_id, qrScan = qrScan)

if __name__ == "__main__":
    app.run
