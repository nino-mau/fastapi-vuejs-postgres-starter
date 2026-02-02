from typing import Annotated
from sqlmodel import SQLModel, Session, create_engine, select
from fastapi import Depends

from models.user import User
from .config import settings

engine = create_engine(settings.database_url)


def db_init():
    # Create tables
    SQLModel.metadata.create_all(engine)

    # Create admin user
    with Session(engine) as session:
        user = session.exec(
            select(User).where(User.email == settings.admin_email)
        ).first()
        if not user:
            default_user = User(name="admin", email="admin@app.com")
            session.add(default_user)
            session.commit()


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
