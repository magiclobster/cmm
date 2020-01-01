#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# module for admin pages
from functools import wraps

from flask import render_template, Blueprint, request
from flask import current_app as app
from unqlite_db import create_user, get_user, get_all_users
from werkzeug.exceptions import abort

root = Blueprint('root', __name__, template_folder='templates')


@root.route('/')
def get_index():
    user_list = get_all_users()
    return render_template('main.html', c=app.config_obj, title="Startseite", lang=app.languages, users=user_list)
