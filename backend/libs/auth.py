import falcon
import hashlib

import config
from models.user import User
from libs.redis import Redis


def get_user(user_session):
    user_id = Redis.get(user_session)

    if not user_id:
        raise falcon.HTTPUnauthorized()

    return (
        User
        .select()
        .where(User.id == user_id)
        .get()
    )


def with_auth(req, resp, resource, params):
    if 'user_session' in req.cookies:
        try:
            user = get_user(req.cookies['user_session'])
            resource.user = user
        except Exception:
            resource.user = None
    else:
        resource.user = None


def auth_required(req, resp, resource, params):

    if 'user_session' not in req.cookies:
        raise falcon.HTTPUnauthorized()

    user = get_user(req.cookies['user_session'])

    if not user:
        raise falcon.HTTPUnauthorized()

    resource.user = user


def admin_required(req, resp, resource, params):
    if 'user_session' not in req.cookies:
        raise falcon.HTTPUnauthorized()

    user = get_user(req.cookies['user_session'])

    if not user:
        raise falcon.HTTPUnauthorized()

    if not user.is_admin:
        raise falcon.HTTPForbidden()

    resource.user = user


def make_session(credential, user_data, user_id):
    user_credential = credential+config.SECURE['secure']['salt_session']+user_data

    session = hashlib.sha256(user_credential.encode()).hexdigest()

    Redis.set(session, user_id)

    return session


def remove_session(session):
    Redis.delete(session)
