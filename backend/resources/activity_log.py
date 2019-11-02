import datetime as dt

import falcon

from sqlalchemy import and_, func, asc, extract
from sqlalchemy.orm import aliased, contains_eager

from models.activity_log import ActivityLog
from models.worker import Worker
from libs.sqlalchemy import Session
from libs.auth import auth_required
from schemas.activity_log import ActivityLogPublicSchema


class ActivityLogController(object):

    @falcon.before(auth_required)
    def on_get(self, req, resp):

        date = req.params['date']

        payload_sum = aliased(ActivityLog)

        logs = Session.query(
                func.sum(payload_sum.payload).label('product_kilogramms'),
                ActivityLog.worker_id.label('worker_id'),
                extract('hour', ActivityLog.local_time).label('work_hour'),
                Worker
            )\
            .join(Worker, Worker.id == ActivityLog.worker_id)\
            .join(payload_sum, ActivityLog.box_code == payload_sum.box_code)\
            .filter(
                and_(
                    ActivityLog.type == 'COLLECT',
                    payload_sum.type == 'REVIEW',
                    func.date(ActivityLog.local_time) >= date,
                    func.date(payload_sum.local_time) <= date
                )
            )\
            .group_by(ActivityLog.worker_id, extract('hour', ActivityLog.local_time), Worker)\
            .order_by(extract('hour', ActivityLog.local_time).asc())\
        
        if not logs.first():
            raise falcon.HTTPNotFound()

        resp.body = ActivityLogPublicSchema(many=True).dumps(logs)
