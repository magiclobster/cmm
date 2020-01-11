#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" This is the Module for the User pages.

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.
This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""
import os

from flask import Flask, request, session
from flask_babel import Babel
from configobj import ConfigObj
from flask_debugtoolbar import DebugToolbarExtension
from views.root import root
from views.user import user
from views.admin import admin


app = Flask(__name__)
app.register_blueprint(root, url_prefix="/")
app.register_blueprint(user, url_prefix="/user")
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

    ret = 'en'
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
    if config['main']['create_test_data']:
        from helpers.create_demo_database import create_demo_db
        create_demo_db('cmm.db', '../helpers/demodata', 25)
    app.run(
        host=os.getenv('BIND_IP', config['main']['server_ip']),
        port=int(os.getenv('BIND_PORT', config['main']['server_port'])))


if __name__ == '__main__':
    run_server()
