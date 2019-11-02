from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from libs.sqlalchemy import CustomQuery, base_model, Session

Base = declarative_base(cls=base_model(Session))
