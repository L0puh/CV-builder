from flask import Flask, session, redirect, url_for
from CVs import user_features
from convert import convert
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['UPLOAD_FILE_PDF'] = 'resume.pdf'
app.config['UPLOAD_FILE_HTML'] = 'resume.html'

app.register_blueprint(user_features.user_func)
app.register_blueprint(convert.convert)

@app.route('/')
def index():
    pdf = app.config['UPLOAD_FILE_PDF']
    html = app.config['UPLOAD_FILE_HTML']
    if 'image' in session:
        os.remove(session['image'])
        if 'file' in session:
            session.clear()
    if os.path.isfile(pdf) and os.path.isfile(html):
        os.remove(html)
        os.remove(pdf)
    return redirect(url_for("user_func.choose_template"))


if '__main__' == __name__:
    app.run(debug=True)
