from flask import Blueprint, render_template

choice_temp=Blueprint('choice_temp', __name__, template_folder='templates/choice_temp')

@choice_temp.route('/choose_temp', methods=['GET', 'POST'])
def choose_template():
    return render_template('choose_temp.html')
