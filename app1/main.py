from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app1.api.routers import notes, ping, users
from app1.config.db import database, engine, metadata

metadata.create_all(engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(ping.router)
app.include_router(notes.router, prefix="/notes", tags=["notes"])
app.include_router(users.router, prefix="/users", tags=["users"])



