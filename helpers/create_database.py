#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os
from cmm.models.tag import Tag, HiddenTag
from cmm.models.user import User


def create_demo_db(data_dir, truncate=False):
    if os.path.isfile('cmm_db.sqlite'):
        if truncate:
            os.remove('cmm_db.sqlite')
    User.create_table()
    Tag.create_table()
    HiddenTag.create_table()
    create_users(data_dir)
    create_tags(data_dir)
    create_hidden_tags(data_dir)


def create_users(data_dir):
    with open(os.path.join(data_dir, 'user.json'), 'r') as f:
        data = f.read()
    user_data = json.loads(data)
    for user in user_data:
        user = User.create(name=user['name'],
                           email=user['mail'],
                           description=user['description'],
                           congress_visits=1,
                           mentor=False
                           )


def create_tags(data_dir):
    with open(os.path.join(data_dir, 'tag.json'), 'r') as f:
        data = f.read()
    tag_data = json.loads(data)
    for tag in tag_data:
        tag = Tag.create(name=tag)


def create_hidden_tags(data_dir):
    with open(os.path.join(data_dir, 'hidden_tag.json'), 'r') as f:
        data = f.read()
    tag_data = json.loads(data)
    for tag in tag_data:
        tag = HiddenTag.create(name=tag)


if __name__ == '__main__':
    create_users('demodata')
