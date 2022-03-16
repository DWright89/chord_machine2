from fastapi import APIRouter
from pydantic import BaseModel
from server.models.database.Users import Users, User_Pydantic


root_router = APIRouter()


@root_router.get("/")
def root():
    """
    This is an example router for examples!!!!
    """
    return {"hello": "world"}
