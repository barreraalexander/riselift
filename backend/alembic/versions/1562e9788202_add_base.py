""" add-base

Revision ID: 1562e9788202
Revises: 
Create Date: 2022-07-19 21:57:44.947127

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1562e9788202'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('worksessions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('session_begin', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('session_end', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('worksessions')
    op.drop_table('users')
    # ### end Alembic commands ###