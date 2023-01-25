from app1.api.schemas.user import UserSchema
from app1.config.db import database
from app1.api.models.users import users


async def post(payload: UserSchema):
    query = users.insert().values(name=payload.name,
                                  email=payload.email,
                                  password=payload.password)
    return await database.execute(query=query)


async def get(id: int):
    query = users.select().where(id == users.c.id)
    return await database.fetch_one(query=query)


async def get_all():
    query = users.select()
    return await database.fetch_all(query=query)


async def put(id: int, payload: UserSchema):
    query = (
        users
            .update()
            .where(id == users.c.id)
            .values(name=payload.name,
                    email=payload.email,
                    password=payload.password)
            .returning(users.c.id)
    )
    return await database.execute(query=query)


async def delete(id: int):
    query = users.delete().where(id == users.c.id)
    return await database.execute(query=query)