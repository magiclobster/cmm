#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import uuid
import os
from unqlite import UnQLite
# include standard modules
import argparse

# initiate the parser
desc = 'This Program creates a demo user database with up to 100 users\nBy default the Program will append to a existing database unless you set the --truncate option.'
parser = argparse.ArgumentParser(description = desc)
parser.add_argument("-n","--number", help="Number of users to create", default="25")
parser.add_argument('-o','--output', help='Path where the database will be stored', default='./cmm.db')
parser.add_argument('-t','--truncate', help='Override existing database', action="store_true")
args=parser.parse_args()

if os.path.isfile(args.output):
    if args.truncate:
        os.remove(args.output)

db = UnQLite(args.output)
users = db.collection('users')
users.create()
with open('demodata/user_demodata.txt','r') as myfile:
    data = myfile.read()
number_of_users = int(args.number)
if number_of_users > 100: number_of_users = 100
dat = json.loads(data)
for d in dat:
    d['id']=uuid.uuid4().hex
    d['active']=True

users.store(dat[:number_of_users])
