from contextlib import asynccontextmanager

from typing import Annotated, Sequence

from fastapi import FastAPI, Query
from sqlmodel import select

from core.db import db_init, SessionDep
from models.user import User


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize db
    db_init()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
def get_root():
    return {"Hello": "World"}


@app.get("/users/")
def get_users(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> Sequence[User]:
    users = session.exec(select(User).offset(offset).limit(limit)).all()
    return users
