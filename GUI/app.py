from flask import Flask, jsonify, render_template, request, make_response, redirect, session, url_for, flash
from flask_wtf.csrf import CSRFProtect, generate_csrf, CSRFError
from datetime import datetime
import os

app = Flask(__name__)
csrf = CSRFProtect(app)
app.config['SECRET_KEY'] = "I wish I could fly"

base = os.path.dirname(os.path.abspath(__file__))
imageFolder = os.path.join(base, 'static', 'images')

#should we do CSRF?
@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    return redirect('/')

@app.route('/')
def mainPage():
   # csrf_token = generate_csrf()
   # user_cookie = request.cookies.get('user_cookie')
   return render_template('index.html',)
   


@app.route('/liveFeed.html', methods = ['GET'])
def liveFeedPage():
   return render_template('liveFeed.html')

@app.route("/gallery.html")
def galleryPage():
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

@app.route('/image/item_id', methods = ['GET'])
def displayImagePage():
   return render_template('displayImage.html')



if __name__ == '__main__':
   app.run(debug=True)
