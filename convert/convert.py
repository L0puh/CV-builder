import os, pdfkit, html_to_json, json
from flask import Blueprint, session, send_file,\
    render_template, send_from_directory, current_app, url_for

convert=Blueprint('convert', __name__, template_folder='templates/convert')

@convert.route('/generate_html/<file_format>')
def generate_html(file_format):
    html = render_template(session['choice'], data=session)
    if file_format == 'pdf':
        return create_pdf(current_app.config['HTML'], html, current_app.config['PDF'])
    return create_json(html, current_app.config['JSON'])

def create_pdf(html_file, html, pdf_file):
    with open(html_file,'w') as f: f.write(html)
    session['file'] = html_to_pdf(html_file, pdf_file)
    return send_from_directory(current_app.root_path,
            pdf_file, as_attachment=True,
            download_name=pdf_file)

def create_json(html, json_file):
    out=html_to_json.convert(html, capture_element_attributes=False)
    with open(json_file, 'w') as f:
        json.dump(out, f)
        session['file']=out
    return send_from_directory(current_app.root_path, json_file)

def html_to_pdf(html_path, pdf_file):
    pdfkit.from_file(html_path, pdf_file,
            options={"enable-local-file-access": ""})
    return True
