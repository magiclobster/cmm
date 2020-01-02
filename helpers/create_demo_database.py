#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import uuid
import os
from unqlite import UnQLite
# include standard modules
import argparse


def parse_args():
    # initiate the parser
    desc = '''
    This Program creates a demo user database with up to 100 users\n
    By default the Program will append to a existing database unless you set the --truncate option.'
    '''
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("-n", "--number", help="Number of users to create", default="25")
    parser.add_argument('-o', '--output', help='Path where the database will be stored', default='./cmm.db')
    parser.add_argument('-d', '--data-path', help='demodata json files', default='demodata')
    parser.add_argument('-t', '--truncate', help='Override existing database', action="store_true")
    return parser.parse_args()


def create_demo_db(db_file, data_path, user_count, truncate=True):
    if os.path.isfile(db_file):
        if truncate:
            os.remove(db_file)
    db = UnQLite(db_file)
    create_users(db, data_path, user_count)
    create_tags(db, data_path)


def create_users(db, data_path, user_count):
    user = db.collection('user')
    user.create()
    with open(os.path.join(data_path, 'user.json'), 'r') as f:
        data = f.read()
    number_of_users = int(user_count)
    if number_of_users > 100:
        number_of_users = 100
    users = json.loads(data)

    # users.store(dat[:number_of_users])
    for u in users[:number_of_users]:
        if 'id' not in u.keys():
            u['id'] = uuid.uuid4().hex
        u['active'] = True
        db_id = user.store(u)
        db[u['id']] = db_id


def create_tags(db, data_path):
    tag = db.collection('tag')
    tag.create()
    with open(os.path.join(data_path, 'tag.json'), 'r') as f:
        data = f.read()
    tags = json.loads(data)
    tag.store(tags)


if __name__ == '__main__':
    args = parse_args()
    create_demo_db(args.output, args.data_path, args.number, args.truncate)
