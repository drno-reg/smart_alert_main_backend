from pydantic import BaseModel


class UserSchema(BaseModel):
    name: str
    email: str
    password: str


class UserDB(UserSchema):
    id: int