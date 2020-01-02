#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Module for the user Pages'''
from flask import render_template, Blueprint, request, session, make_response
from flask import current_app as app
from flask_babel import gettext
from unqlite_db import create_user, get_user, get_all_users, get_tags

user = Blueprint('user', __name__, template_folder='templates')


@user.route('/<user_id>')
def page(user_id):
    user_data = get_user(user_id)
    resp = make_response(render_template("user_profile.html", user=user_data))
    resp.set_cookie('user_id', user_id)
    return resp


@user.route('/register')
def register():
    return render_template("user_register.html", tags=get_tags(), c=app.config_obj, title="Register")


@user.route('/response', methods=['POST'])
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
        "user_register_response.html",
        name=nickname,
        mail=mail,
        description=description,
        tags=chaos_tags,
        user_uuid=user_uuid,
        c=app.config_obj,
        title="Register Response")