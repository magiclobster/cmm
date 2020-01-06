from peewee import Model

from cmm import db


class BaseModel(Model):
    class Meta:
        database = db
