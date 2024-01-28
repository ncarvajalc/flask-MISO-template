from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
import os

engine = create_engine(os.getenv("DATABASE_URL") or "sqlite:///./test.db")
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    import models.user

    Base.metadata.create_all(bind=engine)
