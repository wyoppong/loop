from tortoise import Model, fields
from tortoise.contrib.pydantic import pydantic_model_creator

class User(Model):
    """
    The User model
    """
    id = fields.IntField(pk=True)
    first_name = fields.CharField(max_length=255, null=False)
    last_name = fields.CharField(max_length=255, null=False, index=True)
    email = fields.CharField(max_length=100, null=True)

class PydanticMeta:
    exclude = ["id"]

User_Pydantic = pydantic_model_creator(User, name="User")
UserIn_Pydantic = pydantic_model_creator(User, name="UserIn", exclude_readonly=True)