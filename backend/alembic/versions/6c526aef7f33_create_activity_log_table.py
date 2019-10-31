"""create activity log table

Revision ID: 6c526aef7f33
Revises: 037c4e123dd8
Create Date: 2019-10-29 16:15:53.762044

"""
import datetime as dt

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

import sys
from os.path import abspath, dirname
sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from models.activity_log import ActivityType, ActivityStatus


# revision identifiers, used by Alembic.
revision = '6c526aef7f33'
down_revision = '037c4e123dd8'
branch_labels = None
depends_on = None


def upgrade():

    op.create_table(
        'activity_log',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('box_code', sa.Integer),
        sa.Column('worker_id', sa.Integer, sa.ForeignKey('worker.id')),
        sa.Column('payload', sa.Integer),
        sa.Column('type', postgresql.ENUM(ActivityType, name="activity_type")),
        sa.Column('status', postgresql.ENUM(ActivityStatus, name="status_type")),
        sa.Column('local_time', sa.DateTime()),
        sa.Column('server_time', sa.DateTime(), default=dt.datetime.now())
    )

def downgrade():
    op.drop_table('worker')
