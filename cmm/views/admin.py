#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# module for admin pages
from functools import wraps

from flask import render_template, Blueprint, request
from flask import current_app as app
from unqlite_db import create_user, get_user, get_all_users
from werkzeug.exceptions import abort

admin = Blueprint('admin', __name__, template_folder='templates')


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user_id = request.cookies.get('user_id')
        if not is_admin(user_id):
            return abort(401)
        return f(*args, **kwargs)

    return decorated_function


def is_admin(user_id):
    try:
        user = get_user(user_id)
        if user and user['is_admin']:
            return True
    except KeyError:
        return False
    return False


@admin.route('/users')
@admin_required
def get_index():
    all_users = get_all_users()
    return render_template('admin_user_list.html',
                           c=app.config_obj,
                           title="Startseite",
                           lang=app.languages,
                           users=all_users)
