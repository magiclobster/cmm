#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" This is the admin Module of the CMM.

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

#TODO Revert temporal Change back
@admin.route('/')
#@admin_required
def get_index():
    all_users = get_all_users()
    return render_template('admin_user_list.html',
                           c=app.config_obj,
                           title="Startseite",
                           lang=app.languages,
                           users=all_users)
