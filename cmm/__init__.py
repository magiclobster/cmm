#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Chaosmentors Matchpoint App"""
import os

from flask import Flask, request, session
from flask_babel import Babel
from configobj import ConfigObj
from flask_debugtoolbar import DebugToolbarExtension
from users import users
from admin import admin


app = Flask(__name__)
app.register_blueprint(users, url_prefix="/users")
app.register_blueprint(admin, url_prefix="/admin")

# translations
# Available Languages
app.languages = {'en': 'English', 'de': 'Deutsch'}
app.babel = Babel(app)
app.selected_language = 'en'


@app.babel.localeselector
def get_locale():
    """
    Get the users locale Setting
    """
    if 'lang' in session:
        ret = session['lang']
        session['lang'] = 'de'
    else:
        ret = request.accept_languages.best_match(app.languages.keys())

    #ret = 'en'
    return ret


def run_server():
    """
    Start the Development Server
    """
    print(app.selected_language)
    config = ConfigObj('config/main.config', configspec='config/main.config.spec')
    app.config_obj = config
    app.secret_key = config['app']['secret_key']
    app.debug = config['main']['server_debug']
    DebugToolbarExtension(app)
    app.run(
        host=os.getenv('BIND_IP', config['main']['server_ip']),
        port=int(os.getenv('BIND_PORT', config['main']['server_port'])))


if __name__ == '__main__':
    run_server()
