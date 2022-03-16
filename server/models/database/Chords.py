from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator

class Chords(models.Model):
    id = fields.UUIDField(pk=True)
    user = fields.ForeignKeyField('models.Users', related_name='Chords')
    name = fields.TextField()
    order = fields.IntField()
    degree = fields.IntField()
    extension = fields.TextField()
    inversion = fields.TextField()
    url = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
      table: str = "chords"


Chord_Pydantic = pydantic_model_creator(Chords, name="Chord")
