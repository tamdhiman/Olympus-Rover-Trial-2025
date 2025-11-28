import os
from flask import Flask, jsonify, render_template

imageFolder = os.path.join(os.getcwd(), 'images')
app = Flask(__name__)

@app.route('/mainscreen')
def getLiveFeed():
    #Some code to get the live feed?
    return render_template('mainscreen.html')
@app.route("/gallery")
def getImages():
    imageFiles = os.listdir(imageFolder)
    images = []

    if not imageFiles:
        return render_template('gallery.html', image_name=jsonify([]))
    
    for file in imageFiles:
        if file.lower().endswith('.png'):
            images.append(file)
    image_name = jsonify(images)
    return render_template('gallery.html', image_name = image_name)

@app.route("/displayImage/<int:imageID>")
def displayImage(imageID):
    image_name = imageID
    #Code to get QR Code description (insert later)
    balls = ''

    return render_template('displayimage.html', image_name, balls)
if __name__ == "__main__":
    app.run(debug=True)
