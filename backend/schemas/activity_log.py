from marshmallow import Schema, fields
from marshmallow_enum import EnumField
from schemas.worker import WorkerPublicSchema
from models.activity_log import ActivityType, ActivityStatus


class ActivityLogPublicSchema(Schema):

    id = fields.Integer()

    box_code = fields.Integer()
    worker_id = fields.Integer()
    worker = fields.Nested(WorkerPublicSchema)
    payload = fields.Integer()
    type = EnumField(ActivityType)
    status = EnumField(ActivityStatus)

    local_time = fields.DateTime()

    class Meta:
        type_ = "activity_log"


class ActivityLogNestedSchema(Schema):

    inspector = fields.Nested(ActivityLogPublicSchema)
    collector = fields.Nested(ActivityLogPublicSchema)


class ActivityLogsPublicSchema(Schema):

    working_hours = fields.List(fields.Integer())
    logs = fields.Nested(ActivityLogNestedSchema, many=True)

    class Meta:
        type_ = "activity_logs"
