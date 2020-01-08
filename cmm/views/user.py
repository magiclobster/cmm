#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module for the user Pages
"""
from flask import render_template, Blueprint, request, make_response, flash
from flask import current_app as app

from cmm.models.tag import Tag, TagForm, get_all_tags
from cmm.unqlite_db import create_user, get_user, get_tags
from cmm.models.user import User
from cmm.models.user import UserForm

user = Blueprint('user', __name__, template_folder='templates')


@user.route('/<user_id>')
def page(user_id):
    user_data = get_user(user_id)
    resp = make_response(render_template("user_profile.html", user=user_data))
    resp.set_cookie('user_id', user_id)
    return resp


@user.route('/register')
def register():
    u = User()
    form = UserForm(request.form, obj=u)

    return render_template("user_register_p.html", tags=get_all_tags(), c=app.config_obj, title="Register", form=form)


@user.route('/response', methods=['POST'])
def register_response():
    u = User()
    form = UserForm(request.form, obj=u)
    print(request.form)
    if form.validate():
        u.name = request.form.get("name")
        u.email = request.form.get("email")
        u.description = request.form.get("description")
        u.congress_visits = request.form.get("congress_visits")
        chaos_tags = dict()
        for tag in get_all_tags():
            if request.form.get(tag):
                chaos_tags[tag] = (request.form.get(tag))
        User.save(u)

    return render_template(
        "user_register_response.html",
        user=u,
        c=app.config_obj,
        title="Register Response")
