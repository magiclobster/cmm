#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# module for root pages

from flask import render_template, Blueprint
from flask import current_app as app
from cmm.unqlite_db import get_all_users

root = Blueprint('root', __name__, template_folder='templates')


@root.route('/')
def get_index():
    user_list = get_all_users()
    return render_template('root_main.html', c=app.config_obj, title="Startseite", lang=app.languages, users=user_list)
