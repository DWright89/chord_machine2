from fastapi import APIRouter
from pydantic import BaseModel
from server.models.database.Users import Users, User_Pydantic


user_router = APIRouter()

class UserCreateRequest(BaseModel):
    name: str = "Hippo Von Catte"
    email: str = "hippo@gmail.com"


@user_router.post("/users/create", response_model=User_Pydantic)
async def create_user(request: UserCreateRequest):
    """
    This handles the creation of a new user
    """
    new_user = await Users.create(name=request.name, email=request.email)
    return new_user


@user_router.get("/users/all")
async def get_all_users():
    """
    This returns every user in the users table
    """
    users_list = await Users.all()
    return users_list

@user_router.get("/users/{email}")
async def get_one_user(email: str):
  """
  This will return one user from the URL parameters
  """
  one_user = await Users.get(email=email)
  return one_user