import falcon

from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

from libs.sqlalchemy import CustomQuery

import config


engine = create_engine(
    'postgresql+{engine}://{username}:{password}@{host}:{port}/{db_name}'.format(
        **config.POSTGRESQL
    ),
    pool_size=config.POSTGRESQL['pool_size'],
    echo=config.SQLALCHEMY['debug']
)

session_factory = sessionmaker(bind=engine, query_cls=CustomQuery)
Session = scoped_session(session_factory)

class SQLAlchemySessionManager:

    def __init__(self, Sssion):
        self.db_session = Session

    def process_resource(self, req, resp, resource, params):
        req.context['db_session'] = self.db_session()

    def process_response(self, req, resp, resource, req_succeeded):

        if req.context.get('db_session'):
            if not req_succeeded:
                req.context['db_session'].rollback()
            req.context['db_session'].close()
