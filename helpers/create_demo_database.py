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
    parser.add_argument('-i', '--input', help='demodata json file', default='demodata/user_demodata.json')
    parser.add_argument('-t', '--truncate', help='Override existing database', action="store_true")
    return parser.parse_args()


def create_demo_db(db_file, json_file, user_count, truncate=True):
    if os.path.isfile(db_file):
        if truncate:
            os.remove(db_file)

    db = UnQLite(db_file)
    users = db.collection('users')
    users.create()
    with open(json_file, 'r') as f:
        data = f.read()
    number_of_users = int(user_count)
    if number_of_users > 100:
        number_of_users = 100
    dat = json.loads(data)

    # users.store(dat[:number_of_users])
    for user in dat[:number_of_users]:
        if 'id' not in user.keys():
            user['id'] = uuid.uuid4().hex
        user['active'] = True
        db_id = users.store(user)
        db[user['id']] = db_id


if __name__ == '__main__':
    args = parse_args()
    create_demo_db(args.output, args.input, args.number, args.truncate)
