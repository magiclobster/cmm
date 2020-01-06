#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chaosmentors Matchpoint App
"""
from configobj import ConfigObj
from flask import Flask
from flask_babel import Babel
from peewee import SqliteDatabase

app = Flask(__name__)

config = ConfigObj('config/main.config', configspec='config/main.config.spec')
app.config_obj = config

# translations
# Available Languages
app.languages = {'en': 'English', 'de': 'Deutsch'}
app.babel = Babel(app)
app.selected_language = 'en'

DATABASE = 'cmm_db.sqlite'
db = SqliteDatabase(DATABASE)


