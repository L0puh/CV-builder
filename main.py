from flask import Flask
import CVs.choice_temp as cv

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'

app.register_blueprint(cv.choice_temp)

if '__main__' == __name__:
    app.run(debug=True)
