from flask import render_template, Blueprint
from flask import current_app as app

api = Blueprint('api', __name__, template_folder='templates')


@api.route('/')
def get_index():
    return render_template('main.html', c=app.config_obj)
