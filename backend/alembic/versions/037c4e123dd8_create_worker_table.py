"""create worker table

Revision ID: 037c4e123dd8
Revises: 
Create Date: 2019-10-29 15:37:53.190845

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

import sys
from os.path import abspath, dirname
sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from models.worker import WorkerType


# revision identifiers, used by Alembic.
revision = '037c4e123dd8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():

    op.create_table(
        'worker',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('ean13', sa.Integer, unique=True, nullable=False),
        sa.Column('password', sa.String(20), nullable=False),
        sa.Column('name', sa.String(15)),
        sa.Column('surname', sa.String(15)),
        sa.Column('middle_name', sa.String(15)),
        sa.Column('type', postgresql.ENUM(WorkerType, name="worker_type"), nullable=False),
        sa.Column('deleted', sa.Boolean, default=False, nullable=False)
    )


def downgrade():

    op.drop_table('worker')
