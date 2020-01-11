#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" This is the Module UnQLite Module of the CMM.

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
from unqlite import UnQLite
import uuid

db_file = 'cmm.db'


def get_collection(collection):
    db = UnQLite(db_file)
    collection = db.collection(collection)
    if not collection.exists():
        collection.create()
    return collection


def gen_uuid(length=32):
    u = uuid.uuid4()
    return u.hex[:length]


def get_tags():
    return get_collection('tag').all()


def get_user(user_uuid):
    db = UnQLite(db_file)
    user_col = get_collection('user')
    try:
        return user_col.fetch(db[user_uuid])
    except KeyError:
        return None


def get_all_users():
    return get_collection('user').all()


def create_user(name, mail, description, tags, active=False, is_admin=False):
    user_col = get_collection('user')
    user_uuid = gen_uuid()
    user = {
        'id': user_uuid,
        'name': name,
        'mail': mail,
        'description': description,
        'tags': tags,
        'active': active,
        'is_admin': is_admin
    }
    user_id = user_col.store(user)
    db = UnQLite(db_file)
    db[user_uuid] = user_id
    return user_uuid


def update_user():
    user = users.fetch(0)
    user['active'] = True
    users.update(0, user)


if __name__ == '__main__':
    #db = UnQLite(db_file)
    #uuid = create_user('basti', 'basti@xxx.de', 'asdasdsadsadsa', [], active=True, is_admin=True)
    #print(uuid)
    print(db.collection('users').all())
    #update_user()


