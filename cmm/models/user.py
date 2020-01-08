import datetime

from peewee import CharField, DateTimeField, BooleanField, TextField, ForeignKeyField, IntegerField
from wtfpeewee.orm import model_form

from cmm.models import BaseModel
from cmm.models.tag import Tag


class User(BaseModel):
    name = CharField()
    email = CharField()
    description = TextField()
    congress_visits = IntegerField()
    creation_date = DateTimeField(default=datetime.datetime.now)
    mentor = BooleanField(default=False)
    active = BooleanField(default=False)
    approved = BooleanField(default=False)
    admin = BooleanField(default=False)

    def __unicode__(self):
        return self.username


UserForm = model_form(User, exclude=[
    "approved",
    "active",
    "admin",
    "creation_date"
])


class Interest(BaseModel):
    user = ForeignKeyField(User, backref='tag')
    tag = ForeignKeyField(Tag, backref='user')
    rating = IntegerField()
