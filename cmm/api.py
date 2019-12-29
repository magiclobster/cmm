#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import render_template, Blueprint, request
from flask import current_app as app

from .unqlite_db import create_user, get_user

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


@api.route('/<user_id>')
def page(user_id):
    user = get_user(user_id)
    return render_template("user_profile.html", user=user)


@api.route('/register')
def register():
    return render_template("register.html", tags=tags)


@api.route('/response', methods=['POST'])
def register_response():
    nickname = request.form.get("nickname")
    mail = request.form.get("mail")
    description = request.form.get("description")
    chaos_tags = dict()
    for tag in tags:
        if request.form.get(tag):
            chaos_tags[tag] = (request.form.get(tag))
    user_uuid = create_user(nickname, mail, description, chaos_tags)
    return render_template("register_response.html", name=nickname, mail=mail, description=description, tags=chaos_tags, user_uuid=user_uuid)
