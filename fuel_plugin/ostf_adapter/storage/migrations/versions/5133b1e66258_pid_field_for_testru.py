"""pid_field_for_testrun

Revision ID: 5133b1e66258
Revises: 53af7c2d9ccc
Create Date: 2014-02-14 16:34:18.751738

"""

# revision identifiers, used by Alembic.
revision = '5133b1e66258'
down_revision = '53af7c2d9ccc'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('test_runs', sa.Column('pid', sa.Integer(), nullable=True))


def downgrade():
    op.drop_column('test_runs', 'pid')
