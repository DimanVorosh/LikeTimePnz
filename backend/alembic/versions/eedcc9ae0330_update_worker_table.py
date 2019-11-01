"""update worker table

Revision ID: eedcc9ae0330
Revises: 6c526aef7f33
Create Date: 2019-11-01 10:06:31.873222

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eedcc9ae0330'
down_revision = '6c526aef7f33'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('worker', sa.Column('login', sa.String(20), unique=True))


def downgrade():
    op.drop_column('worker', 'login')
