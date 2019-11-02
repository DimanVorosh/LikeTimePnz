import falcon
import hashlib

from config import SECURE
from models.worker import Worker
from libs.sqlalchemy import Session
from libs.redis import Redis


def get_user(user_session):

    user_id = Redis.get(user_session)

    if not user_id:
        raise falcon.HTTPUnauthorized()

    return Session.query(Worker)\
        .filter(
            Worker.id == int(user_id)
        ).first()


def auth_required(req, resp, resource, params):

    if 'user_session' not in req.cookies:
        raise falcon.HTTPUnauthorized()

    user = get_user(req.cookies['user_session'])

    if not user:
        raise falcon.HTTPUnauthorized()

    resource.user = user


def make_session(credential, user_data, user_id):

    user_credential = credential+SECURE['salt_session']+user_data

    session = hashlib.sha256(user_credential.encode()).hexdigest()

    Redis.set(session, user_id)

    return session


def remove_session(session):
    Redis.delete(session)
