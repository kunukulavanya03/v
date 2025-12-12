from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, scoped_session
from sqlalchemy.orm.session import sessionmaker
from app.models import Base

engine = create_engine('sqlite:///app.db')
Base.metadata.create_all(engine)
