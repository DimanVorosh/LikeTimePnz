from resources.index import *
from resources.activity_log import *
from resources.login import *
# from resources.case import *


def make_route(app):

    app.add_route('/', IndexController())

    app.add_route('/activity', ActivityLogController())
    app.add_route('/login', WorkerLoginController())
    # app.add_route('/users/current', CurrentUserController())
    # app.add_route('/cases', CasesController())
