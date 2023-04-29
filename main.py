from flask import Flask
from CVs import user_features


app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'

app.register_blueprint(user_features.user_func)

if '__main__' == __name__:
    app.run(debug=True)
