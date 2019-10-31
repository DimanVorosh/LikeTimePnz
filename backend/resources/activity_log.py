import datetime as dt

import falcon

from sqlalchemy import and_, func, asc, extract
from sqlalchemy.orm import aliased

from models.activity_log import ActivityLog
from models.worker import Worker
from libs.middleware import Session
from schemas.activity_log import ActivityLogsPublicSchema


class ActivityLogController(object):

    def on_get(self, req, resp):

        date = req.params['date']

        collector_log = aliased(ActivityLog)

        logs = Session.query(ActivityLog, collector_log)\
            .filter(
                and_(
                    func.date(ActivityLog.local_time) >= date,
                    func.date(ActivityLog.local_time) <= date, 
                    ActivityLog.type == 'REVIEW',
                    ActivityLog.status == 'SUCCESS'
                )
            )\
            .order_by(ActivityLog.local_time.asc())\
            .join(
                collector_log, collector_log.box_code == ActivityLog.box_code
            )\
            .filter(
                and_(
                    collector_log.type == 'COLLECT',
                    collector_log.status == 'SUCCESS',
                    func.date(collector_log.local_time) == func.date(ActivityLog.local_time),
                    extract('hour', collector_log.local_time) == extract('hour', ActivityLog.local_time)
                )
            )

        working_hours = []
        activity_logs = []

        for log in logs:
            working_hours.extend([
                log[0].local_time.hour, 
                log[1].local_time.hour
            ])
            activity_logs.append({
                'inspector': log[0],
                'collector': log[1]
            })

        if working_hours.__len__() == 0:
            raise falcon.HTTPNotFound()

        working_hours = list(set(working_hours))

        result = { 
            'working_hours': working_hours,
            'logs': activity_logs
        }

        resp.body = ActivityLogsPublicSchema().dumps(result)
