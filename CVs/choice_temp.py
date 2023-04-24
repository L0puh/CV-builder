from flask import Blueprint, render_template, session, url_for, redirect
from forms import Choice_temp

choice_temp=Blueprint('choice_temp', __name__,
        template_folder='templates/choice_temp')


@choice_temp.route('/choose_temp', methods=['GET', 'POST'])
def choose_template():
    form=Choice_temp()
    if form.validate_on_submit:
        choice=form.choice.data
        session['choice']=choice
        if choice: return redirect(url_for('.get_user_data'))
    return render_template('choose_temp.html', form=form)

@choice_temp.route('/get_user_data', methods=['GET', 'POST'])
def get_user_data():
    return render_template('get_user_data.html')
