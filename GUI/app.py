from flask import Flask, render_template, request, make_response, redirect, session, url_for, flash
from flask_wtf.csrf import CSRFProtect, generate_csrf, CSRFError
from datetime import datetime


app = Flask(__name__)
csrf = CSRFProtect(app)
app.config['SECRET_KEY'] = "I wish I could fly"

#should we do CSRF?
@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    return redirect('/')

@app.route('/')
def mainPage():
   # csrf_token = generate_csrf()
   # user_cookie = request.cookies.get('user_cookie')
   return render_template('index.html',)


@app.route('/liveFeed', methods = ['GET'])
def liveFeedPage():
   return render_template('liveFeed.html')

@app.route('/gallery')
def galleryPage():
   return render_template('gallery.html')

@app.route('/image/item_id', methods = ['GET'])
def displayImagePage():
   return render_template('displayImage.html')



if __name__ == '__main__':
    app.run(debug=True)
