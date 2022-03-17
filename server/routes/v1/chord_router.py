from fastapi import APIRouter
from pydantic import BaseModel
from server.models.database.Chords import Chords, Chord_Pydantic
from server.models.database.Users import Users, User_Pydantic
from typing import List
from uuid import UUID
from loguru import logger

chord_router = APIRouter()


class ChordCreateRequest(BaseModel):
    order: int
    degree: int
    extension: str
    inversion: str
    url: str


class ChordList(BaseModel):
    user_id: str = "5bb95d65-36b1-4322-833e-a1ef1e7933d2"
    name: str = "hippohop"
    chord_list: List[ChordCreateRequest]


@chord_router.post("/chords/create", response_model=ChordList)
async def create_chords(request: ChordList):
    """
    Creates chord sequence for a given user
    """
    user = await Users.get(id=request.user_id)
    logger.info(user)
    for chord in request.chord_list:
        await Chords.create(
            user=user.id,
            name=request.name,
            order=chord.order,
            degree=chord.degree,
            extension=chord.extension,
            inversion=chord.inversion,
            url=chord.url,
        )
    return 'done'
