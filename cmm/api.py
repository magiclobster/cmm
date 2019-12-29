#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import render_template, Blueprint, request
from flask import current_app as app

api = Blueprint('api', __name__, template_folder='templates')

tags = [
    'lockpicking',
    'hacking',
    'soldering',
    'dancing',
    'music'
        ]


@api.route('/')
def get_index():
    return render_template('main.html', c=app.config_obj, title="Startseite")


@api.route('/register')
def register():
    return render_template("register.html", tags=tags)


@api.route('/response', methods=['POST'])
def register_response():
    nickname = request.form.get("nickname")
    description = request.form.get("description")
    return render_template("register_response.html", name=nickname, description=description)
