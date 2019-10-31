from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from libs.sqlalchemy import CustomQuery, base_model

DBSession = scoped_session(sessionmaker(query_cls=CustomQuery))
Base = declarative_base(cls=base_model(DBSession))
