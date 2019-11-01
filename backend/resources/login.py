import falcon

from sqlalchemy import and_, func, asc, extract
from sqlalchemy.orm import aliased, contains_eager

from libs.decorators import with_body_params
from libs.middleware import Session
from libs.auth import make_session
from models.worker import *
from schemas.worker import WorkerLoginSchema


class WorkerLoginController(object):

  @with_body_params(WorkerLoginSchema)
  def on_post(self, req, resp):

    login = req.parsed['login'],
    password = req.parsed['password']

    try:
      worker = Session.query(Worker)\
        .filter(
            Worker.login == login
        ).first()
    except Exception:
      raise falcon.HTTPNotFound()

    if not worker.is_password_valid(password):
      raise falcon.HTTPUnauthorized()

    if worker.type != WorkerType.INSPECTOR:
      raise falcon.HTTPBadRequest()

    try:
      resp.set_cookie(
          'user_session',
          make_session(
              credential=login[0],
              user_data=req.host+req.user_agent,
              user_id=worker.id
          ),
          path='/'
      )
    except Exception:
      raise falcon.HTTPUnauthorized()
