from peewee import CharField, ForeignKeyField
from cmm.models import BaseModel


class Tag(BaseModel):
    name = CharField()

    def __unicode__(self):
        return self.name
