#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from unqlite import UnQLite
import uuid

db = UnQLite()


users = db.collection('users')
users.create()


def gen_uuid(length=32):
    u = uuid.uuid4()
    return u.hex[:length]


def create_user(name):
    user_uuid = gen_uuid()
    user = {'id': user_uuid, 'name': name}
    user_id = users.store(user)
    db[user_uuid] = user_id


if __name__ == '__main__':
    create_user('basti')
    print(users.all())
    print([item for item in db])


