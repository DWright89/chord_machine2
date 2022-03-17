from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator

class Users(models.Model):
    id = fields.UUIDField(pk=True)
    email = fields.TextField()
    name = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table: str = "users"

User_Pydantic = pydantic_model_creator(Users, name="User")