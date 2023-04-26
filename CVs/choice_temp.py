import os
from flask import Blueprint, render_template, session,\
        url_for, redirect, make_response
from forms import Choice_temp_form, Input_data_form
from werkzeug.utils import secure_filename

choice_temp=Blueprint('choice_temp', __name__,
        template_folder='templates/choice_temp')
upload_folder='static/uploads'

@choice_temp.route('/choose_temp', methods=['GET', 'POST'])
def choose_template():
    form=Choice_temp_form()
    if form.validate_on_submit:
        choice=form.choice.data
        session['choice']=choice
        if choice: return redirect(url_for('.get_user_data'))
    return render_template('choose_temp.html', form=form)

@choice_temp.route('/get_user_data/', methods=['GET', 'POST'])
def get_user_data():
    form=Input_data_form()
    if form.validate_on_submit():
        file=form.image.data
        filename=secure_filename(file.filename)
        file.save(os.path.join(upload_folder, filename))

        session['name']=form.name.data
        session['email']=form.email.data
        session['about']=form.about.data
        session['image']=os.path.join(upload_folder, filename)
        return redirect(url_for('.test'))
    return render_template('get_user_data.html', form=form)

@choice_temp.route('/test')
def test():
    image=(f'{os.path.join(session["image"])}')
    return render_template('test.html', image=image, name=session['name'])

