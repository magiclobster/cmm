#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" This is the root Module of the CMM.

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

root = Blueprint('root', __name__, template_folder='templates')


@root.route('/')
def get_index():
    user_list = get_all_users()
    return render_template('root_main.html', c=app.config_obj, title="Startseite", lang=app.languages, users=user_list)
