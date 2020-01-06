#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import uuid
import os
from unqlite import UnQLite
# include standard modules
import argparse

from cmm.models.tag import Tag
from cmm.models.user import User


def create_demo_db(data_dir, truncate=False):
    if os.path.isfile('cmm_db.sqlite'):
        if truncate:
            os.remove('cmm_db.sqlite')
    User.create_table()
    Tag.create_table()
    create_users(data_dir)
    create_tags(data_dir)


def create_users(data_dir):
    with open(os.path.join(data_dir, 'user.json'), 'r') as f:
        data = f.read()
    user_data = json.loads(data)
    for user in user_data:
        user = User.create(username=user['name'], email=user['mail'], description=user['description'])


def create_tags(data_dir):
    with open(os.path.join(data_dir, 'tag.json'), 'r') as f:
        data = f.read()
    tag_data = json.loads(data)
    for tag in tag_data:
        tag = Tag.create(name=tag)


if __name__ == '__main__':
    create_users('demodata')
