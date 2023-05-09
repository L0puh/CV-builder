from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, StringField, \
        FileField, EmailField, TextAreaField, RadioField

class Choice_temp_form(FlaskForm):
    choice=RadioField(choices=[('temp1', 'temp1'), ('temp2', 'temp2')])
    submit=SubmitField()
class Input_data_form(FlaskForm):
    name=StringField()
    image=FileField()
    email=EmailField()
    about=TextAreaField()
    skills=TextAreaField()
    work_experience=TextAreaField()
    education=TextAreaField()
    file_format=SelectField(choices=['json', 'pdf'])
    submit=SubmitField()

