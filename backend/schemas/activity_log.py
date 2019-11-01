from marshmallow import Schema, fields
from marshmallow_enum import EnumField
from schemas.worker import WorkerPublicSchema
from models.activity_log import ActivityType, ActivityStatus


class ActivityLogSchema(Schema):
  
    product_kilogramms = fields.Integer()
    worker_id = fields.Integer()
    work_hour = fields.Integer()
    Worker = fields.Nested(WorkerPublicSchema)


class ActivityLogsPublicSchema(Schema):

    working_hours = fields.List(fields.Integer())
    logs = fields.Nested(ActivityLogSchema, many=True)

    class Meta:
        type_ = "activity_logs"
