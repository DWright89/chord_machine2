from tortoise import fields, models


class Users(models.Model):
    id = fields.UUIDField(pk=True)
    email = fields.TextField()
    name = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table: str = "users"
