from flask import (

    Blueprint, render_template, request, url_for
)



from flask.helpers import url_for
from flask.templating import render_template
from werkzeug.utils import redirect

bp = Blueprint('portfolio', __name__, url_prefix='/')

@bp.route('/', methods=['GET'])
def index():
    return render_template('portfolio/index.html')


@bp.route('/mail', methods=['GET','POST'])
def mail():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    if request.method == 'POST':     
        send_email(name, email, message)
        return render_template('portfolio/sent_mail-html')

    return redirect(url_for('portfolio.index'))

def send_email(name, email, message):
    mi_email = 'david159134@hotmail.com'
 
      