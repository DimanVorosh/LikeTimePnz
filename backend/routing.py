from resources.index import *
from resources.activity_log import *
from resources.auth import *


def make_route(app):

    app.add_route('/', IndexController())

    app.add_route('/activity', ActivityLogController())
    app.add_route('/login', WorkerLoginController())
    app.add_route('/logout', LogoutController())
    app.add_route('/users/current', CurrentWorkerController())
