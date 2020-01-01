#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Module for the user Pages'''
from flask import render_template, Blueprint, request, session
from flask import current_app as app
from flask_babel import gettext
from unqlite_db import create_user, get_user, get_all_users

users = Blueprint('users', __name__, template_folder='templates')

tags = [
    'lockpicking',
    'hacking',
    'soldering',
    'dancing',
    'music'
        ]


@users.route('/')
def get_index():
    userlist = get_all_users()
    return render_template('main.html', c=app.config_obj, title="Startseite", lang = app.languages, users=userlist)


@users.route('/<user_id>')
def page(user_id):
    user = get_user(user_id)
    return render_template("users_profile.html", user=user)


@users.route('/register')
def register():
    return render_template("users_register.html", tags=tags, c=app.config_obj, title="Register")


@users.route('/response', methods=['POST'])
def register_response():
    nickname = request.form.get("nickname")
    mail = request.form.get("mail")
    description = request.form.get("description")
    chaos_tags = dict()
    for tag in tags:
        if request.form.get(tag):
            chaos_tags[tag] = (request.form.get(tag))
    user_uuid = create_user(nickname, mail, description, chaos_tags)
    return render_template(
        "users_register_response.html",
        name=nickname,
        mail=mail,
        description=description,
        tags=chaos_tags,
        user_uuid=user_uuid,
        c=app.config_obj,
        title="Register Response")
