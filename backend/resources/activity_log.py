import datetime as dt

import falcon

from sqlalchemy import and_, func, asc, extract
from sqlalchemy.orm import aliased, contains_eager

from models.activity_log import ActivityLog
from models.worker import Worker
from libs.middleware import Session
from schemas.activity_log import ActivityLogsPublicSchema


class ActivityLogController(object):

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
        
        working_hours = []

        for log in logs:
            print(log[3].__dir__())
            working_hours.append(log[2])
    
        if working_hours.__len__() == 0:
            raise falcon.HTTPNotFound()

        working_hours = list(set(working_hours))

        result = { 
            'working_hours': working_hours,
            'logs': logs
        }

        resp.body = ActivityLogsPublicSchema().dumps(result)
