"""drop exercises from worksessions

Revision ID: 8d0acdd92082
Revises: 28f303f9dd2b
Create Date: 2022-08-15 20:28:57.112989

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d0acdd92082'
down_revision = '28f303f9dd2b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_column('worksessions', 'exercises')


def downgrade() -> None:
    op.add_column('worksessions', 'exercises', sa.String(), nullable=True)
