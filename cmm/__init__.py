#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

from flask import Flask, request
from configobj import ConfigObj
from cmm.users import users
from flask_babel import Babel

app = Flask(__name__)
app.register_blueprint(users, url_prefix="/users")

# translations
# Available Languages
app.languages = {'en_EN': 'English','de_DE': 'German'}
app.babel = Babel(app)

app.selected_language = 'en'

@app.babel.localeselector
def get_locale():
    #ret = request.accept_languages.best_match(app.languages.keys())
    ret = 'en'
    return ret

def run_server():
    print(app.selected_language)
    config = ConfigObj('config/main.config', configspec='config/main.config.spec')
    app.config_obj = config
    app.run(
        host=os.getenv('BIND_IP', config['main']['server_ip']),
        port=int(os.getenv('BIND_PORT', config['main']['server_port'])),
        debug=config['main']['server_debug'])


if __name__ == '__main__':
    run_server()
