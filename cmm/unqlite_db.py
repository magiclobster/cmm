#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from unqlite import UnQLite
import uuid


def get_or_create_db():
    db = UnQLite('cmm.db')
    users = db.collection('users')
    if not users.exists():
        users.create()
    return db


def gen_uuid(length=32):
    u = uuid.uuid4()
    return u.hex[:length]


def get_user(user_uuid):
    db = get_or_create_db()
    try:
        return db.collection('users').fetch(db[user_uuid])
    except KeyError:
        return None


def get_all_users():
    db = get_or_create_db()
    try:
        return db.collection('users').all()
    except KeyError:
        return None


def create_user(name, mail, description, tags, active=False, is_admin=False):
    db = get_or_create_db()
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
    user_id = db.collection('users').store(user)
    db[user_uuid] = user_id
    return user_uuid


def update_user():
    user = users.fetch(0)
    user['active'] = True
    users.update(0, user)


if __name__ == '__main__':
    # db = get_or_create_db()
    uuid = create_user('basti', 'basti@xxx.de', 'asdasdsadsadsa', [], active=True, is_admin=True)
    print(uuid)
    #print(db.collection('users').all())
    #update_user()


