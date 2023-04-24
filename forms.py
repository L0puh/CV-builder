from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField

class Choice_temp(FlaskForm):
    choice=SelectField(choices=['temp1', 'temp2'])
    submit=SubmitField()


