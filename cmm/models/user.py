import datetime

from peewee import CharField, DateTimeField, BooleanField, TextField, ForeignKeyField
from wtfpeewee.orm import model_form

from cmm.models import BaseModel
from cmm.models.tag import Tag


class User(BaseModel):
    username = CharField()
    email = CharField()
    description = TextField()
    creation_date = DateTimeField(default=datetime.datetime.now)
    active = BooleanField(default=True)
    admin = BooleanField(default=False)

    def __unicode__(self):
        return self.username


UserForm = model_form(User, exclude=["active", "admin", "creation_date"])


class Interest(BaseModel):
    user = ForeignKeyField(User, backref='tag')
    tag = ForeignKeyField(Tag, backref='user')
