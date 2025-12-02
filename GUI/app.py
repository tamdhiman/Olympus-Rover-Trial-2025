from flask import Flask, jsonify, render_template, request, make_response, redirect, session, url_for, flash
from flask_wtf.csrf import CSRFProtect, generate_csrf, CSRFError
from datetime import datetime
from backend_py.Gallery import Gallery
from backend_py.Image import Image
import os

app = Flask(__name__)
gallery = Gallery()
csrf = CSRFProtect(app)
app.config['SECRET_KEY'] = "I wish I could fly"

base = os.path.dirname(os.path.abspath(__file__))
imageFolder = os.path.join(base, 'static', 'images')

#should we do CSRF?
@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    return redirect('/')


# HTML PAGES

@app.route('/')
def mainPage():
   # csrf_token = generate_csrf()
   # user_cookie = request.cookies.get('user_cookie')
   csrf_token = generate_csrf()
   return render_template('index.html', csrf_token = csrf_token)

@app.route('/liveFeed.html', methods = ['GET'])
def liveFeedPage():
   return render_template('liveFeed.html')


@app.route("/gallery.html")
def galleryPage():
   images = [img.file_path for img in gallery.images]
   return render_template('gallery.html', image_name = images)

@app.route('/image/item_id', methods = ['GET'])
def displayImagePage():
   return render_template('displayImage.html')


# Call Methods

@app.route('/rover_movement', methods = ['POST'])
def move_rover():
   button_id = request.json.get("button_id")
   print("Python received button press:", button_id)

   # Add movemenet functionality
   
   return jsonify({"status": "ok"})

@app.route('/rover_photo_capture', methods = ['POST'])
def photo_rover():
   print("Python received button press to take a photo")

   # Add photo capture functionality
   # Calls unto add image function?
   
   return jsonify({"status": "ok"})

# Add image function?
gallery.add_image(Image("1", "/static/images/test_1.jpg"))
gallery.add_image(Image("2", "/static/images/test_2.jpg"))
gallery.add_image(Image("3", "/static/images/test_3.jpg"))
gallery.add_image(Image("4", "/static/images/test_4.jpg"))


if __name__ == '__main__':
   app.run(debug=True)
