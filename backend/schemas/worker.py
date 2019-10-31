from marshmallow import Schema, fields
from marshmallow_enum import EnumField
from models.worker import WorkerType


class WorkerPublicSchema(Schema):

    id = fields.Integer()

    ean13 = fields.Integer()

    name = fields.String()
    surname = fields.String()
    middle_name = fields.String()

    type = EnumField(WorkerType)

    deleted = fields.Boolean()

    class Meta:
        type_ = "worker"
