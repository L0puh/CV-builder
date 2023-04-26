from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, StringField, \
        FileField, EmailField, TextAreaField

class Choice_temp_form(FlaskForm):
    choice=SelectField(choices=['temp1', 'temp2'])
    submit=SubmitField()
class Input_data_form(FlaskForm):
    name=StringField()
    image=FileField()
    email=EmailField()
    about=TextAreaField()
    submit=SubmitField()

