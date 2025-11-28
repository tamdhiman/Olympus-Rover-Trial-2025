import os
from flask import Flask, jsonify, render_template

base = os.path.dirname(os.path.abspath(__file__))
imageFolder = os.path.join(base, 'static', 'images')
app = Flask(__name__)

@app.route('/mainscreen.html')
def getLiveFeed():
    #Some code to get the live feed?
    return render_template('/mainscreen.html')

@app.route("/gallery.html")
def getImages():
    imageFiles = os.listdir(imageFolder)
    images = []

    if not imageFiles:
        return render_template('gallery.html', image_name=[])
    
    for file in imageFiles:
        if file.lower().endswith('.png'):
            filePath = f"/static/images/{file}"
            images.append(filePath)
    image_name = jsonify(images)
    return render_template('gallery.html', image_name = images)

@app.route("/displayimage.html")
def displayImage(imageID):
    image_name = imageID
    #Code to get QR Code description (insert later)
    balls = ''

    return render_template('displayimage.html', image_name, balls)
if __name__ == "__main__":
    app.run(debug=True)
