import os, pdfkit
from flask import Blueprint, session, send_file,\
    render_template, send_from_directory, current_app

convert=Blueprint('convert', __name__, template_folder='templates/convert')

@convert.route('/generate_html')
def generate_html():
    html_file=current_app.config['UPLOAD_FILE_HTML']
    pdf_file=current_app.config['UPLOAD_FILE_PDF']
    image=os.path.join(session["image"])
    template = session['choice']
    with open(html_file,'w') as f:
        f.write(render_template(template,
            image=image, name=session['name'],
            email=session['email'], about=session['about'],
            skills=session['skills'], edu=session['edu'],
            work=session['work_exp']))

    out=html_to_pdf(html_file, pdf_file)
    if out:
        session['file'] = out
        return send_from_directory(current_app.root_path,
                pdf_file, as_attachment=True,
                download_name=pdf_file)

def html_to_pdf(html_path, pdf_file):
    pdfkit.from_file(html_path, pdf_file,
            options={"enable-local-file-access": ""})
    return True

