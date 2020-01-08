#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Chaosmentors Matchpoint App"""
import os
from flask import request, session
from flask_debugtoolbar import DebugToolbarExtension
from cmm import app
from cmm.views.root import root as root
from cmm.views.user import user as user
from cmm.views.admin import admin as admin
import flask_admin
from flask_admin.contrib.peewee import ModelView

from cmm.models.tag import Tag, HiddenTag
from cmm.models.user import User


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


def setup_db():
    if app.config_obj['main']['create_test_data']:
        from helpers.create_database import create_demo_db
        create_demo_db('../helpers/demodata', truncate=True)


def register_blueprints():
    app.register_blueprint(root, url_prefix="/")
    app.register_blueprint(user, url_prefix="/user")
    app.register_blueprint(admin, url_prefix="/admin")


def setup_admin():
    adm = flask_admin.Admin(app, name='CMM: admin', endpoint='admin')
    adm.add_view(ModelView(User, endpoint='users'))
    adm.add_view(ModelView(Tag, endpoint='tags'))
    adm.add_view(ModelView(HiddenTag, endpoint='hiddentags'))


def run_server():
    """
    Start the Development Server
    """
    print(app.selected_language)
    app.secret_key = app.config_obj['app']['secret_key']
    app.debug = app.config_obj['main']['server_debug']
    DebugToolbarExtension(app)

    setup_db()
    setup_admin()
    register_blueprints()

    app.run(
        host=os.getenv('BIND_IP', app.config_obj['main']['server_ip']),
        port=int(os.getenv('BIND_PORT', app.config_obj['main']['server_port'])))


if __name__ == '__main__':
    run_server()
