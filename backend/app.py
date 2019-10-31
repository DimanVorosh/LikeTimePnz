import falcon


from libs.middleware import *
from routing import make_route


app = falcon.API(
    middleware=[SQLAlchemySessionManager(Session)],
)

app.req_options.auto_parse_form_urlencoded = True
app.resp_options.secure_cookies_by_default = False

make_route(app)
