from peewee import CharField
from wtforms import Form, RadioField

from cmm.models import BaseModel


def get_all_tags():
    return [tag.name for tag in Tag.select(Tag.name)]


class Tag(BaseModel):
    name = CharField()

    def __unicode__(self):
        return self.name


class TagForm(Form):
    forms = list()
    for tag in ['a', 'b', 'c']:
        forms.append(RadioField(tag, choices=[('0', 'no'), ('1', 'maybe'), ('2', 'sure')]))


class HiddenTag(BaseModel):
    name = CharField()

    def __unicode__(self):
        return self.name
