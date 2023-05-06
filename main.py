from flask import Flask, session, redirect, url_for
from CVs import user_features
from convert import convert
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['PDF'] = 'resume.pdf'
app.config['HTML'] = 'resume.html'
app.config['JSON'] = 'resume.json'

app.register_blueprint(user_features.user_func)
app.register_blueprint(convert.convert)

def delete(pdf, json, html):
    if 'image' in session:
        os.remove(session['image'])
        session.clear()
    if os.path.isfile(pdf) and os.path.isfile(html):
        os.remove(html)
        os.remove(pdf)
    if os.path.isfile(json):
        os.remove(json)
    return True

@app.route('/')
def index():
    delete(app.config['PDF'], app.config['JSON'], app.config['HTML'])
    return redirect(url_for("user_func.choose_template"))

if '__main__' == __name__:
    app.run(debug=True)
