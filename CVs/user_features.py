import os
from flask import Blueprint, render_template, session,\
        url_for, redirect, make_response, send_file
from forms import Choice_temp_form, Input_data_form
from werkzeug.utils import secure_filename
import pdfkit

user_func=Blueprint('user_func', __name__,
        template_folder='templates/user_features')

upload_folder='static/uploads'
wkthmltopdf_path='.venv/lib/wkhtmltopdf/bin/wkhtmltopdf.exe'


@user_func.route('/choose_temp', methods=['GET', 'POST'])
def choose_template():
    form=Choice_temp_form()
    if form.validate_on_submit:
        choice=form.choice.data
        session['choice']=choice
        if choice: return redirect(url_for('.get_user_data'))
    return render_template('choose_temp.html', form=form)

@user_func.route('/get_user_data/', methods=['GET', 'POST'])
def get_user_data():
    form=Input_data_form()
    if form.validate_on_submit():
        file=form.image.data
        filename=secure_filename(file.filename)
        file.save(os.path.join(upload_folder, filename))

        session['name']=form.name.data
        session['email']=form.email.data
        session['about']=form.about.data
        session['work_exp']=form.work_experience.data
        session['edu']=form.education.data
        session['skills']=form.skills.data
        session['image']=os.path.join(upload_folder, filename)
        return redirect(url_for('.generate_html'))
    return render_template('get_user_data.html', form=form)

@user_func.route('/generate_html')
def generate_html():
    image=os.path.join(user_func.root_path, session["image"])
    out=html_to_pdf(render_template('test.html', image=image, name=session['name'],
            email=session['email'], about=session['about'], skills=session['skills'],
            edu=session['edu'], work=session['work_exp']))
    return out

def html_to_pdf(html_path):
    config = pdfkit.configuration(wkhtmltopdf=f'{os.path.join(wkthmltopdf_path)}')
    pdf = pdfkit.from_string(html_path, False,
            configuration=config,
            options={"enable-local-file-access": ""})

    response = make_response(pdf)
    response.headers["Content-Type"] = "application/pdf"
    response.headers["Content-Disposition"] = "inline; filename=output.pdf"
    return response
