"""add exercises to worksession

Revision ID: 4f009b4d27e3
Revises: f8eaa323535e
Create Date: 2022-08-05 20:03:35.980625

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f009b4d27e3'
down_revision = 'f8eaa323535e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('worksessions', sa.Column('exercises', sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_column('worksessions', sa.Column('exercises'))
