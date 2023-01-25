from app1.api.crud import users
from app1.api.schemas.user import UserDB, UserSchema
from typing import List
from fastapi import APIRouter, HTTPException, Path

router = APIRouter()


@router.post("/", response_model=UserDB, status_code=201)
async def create_note(payload: UserSchema):
    user_id = await users.post(payload)

    response_object = {
        "id": user_id,
        "name": payload.name,
        "email": payload.email,
        "password": payload.password
    }
    return response_object


@router.get("/{id}/", response_model=UserDB)
async def read_note(id: int = Path(..., gt=0),):
    user = await users.get(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/", response_model=List[UserDB])
async def read_all_notes():
    return await users.get_all()


@router.put("/{id}/", response_model=UserDB)
async def update_note(payload: UserSchema, id: int = Path(..., gt=0),):
    user = await users.get(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user_id = await users.put(id, payload)

    response_object = {
        "id": user_id,
        "name": payload.name,
        "email": payload.email,
        "password": payload.password
    }
    return response_object


@router.delete("/{id}/", response_model=UserDB)
async def delete_note(id: int = Path(..., gt=0)):
    user = await users.get(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    await users.delete(id)

    return user