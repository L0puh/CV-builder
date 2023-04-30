from flask import Flask
from CVs import user_features
from convert import convert

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'
app.config['ULOAD_FOLDER'] = 'static/uploads'
app.config['UPLOAD_FILE_PDF'] = 'resume.pdf'
app.config['UPLOAD_FILE_HTML'] = 'resure.html'

app.register_blueprint(user_features.user_func)
app.register_blueprint(convert.convert)

if '__main__' == __name__:
    app.run(debug=True)

