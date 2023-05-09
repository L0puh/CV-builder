import os
from flask import Blueprint, render_template, session,\
        url_for, redirect, make_response, send_file,\
        current_app, flash
from forms import Choice_temp_form, Input_data_form
from werkzeug.utils import secure_filename
import pdfkit

user_func=Blueprint('user_func', __name__,
        template_folder='templates/user_features')


@user_func.route('/choose_temp', methods=['GET', 'POST'])
def choose_template():
    form=Choice_temp_form()
    if form.validate_on_submit:
        choice=form.choice.data
        session['choice']=f'{choice}.html'
        if choice: return redirect(url_for('.get_user_data'))
    return render_template('choose_temp.html', form=form)

@user_func.route('/get_user_data/', methods=['GET', 'POST'])
def get_user_data():
    form=Input_data_form()
    if form.validate_on_submit():
        file=form.image.data
        if file:
            filename=secure_filename(file.filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))

            session['name']=form.name.data
            session['email']=form.email.data
            session['about']=form.about.data
            session['work_exp']=form.work_experience.data
            session['edu']=form.education.data
            session['skills']=form.skills.data

            session['image']=os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            return redirect(url_for('convert.generate_html', file_format=form.file_format.data))
        else:flash('attach a photo', 'error')
    return render_template('get_user_data.html', form=form)
