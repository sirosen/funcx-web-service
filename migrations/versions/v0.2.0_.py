"""empty message

Revision ID: v0.2.0
Revises: v0.0.3
Create Date: 2021-05-10 13:23:28.011569

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy import Column, String

revision = 'v0.2.0'
down_revision = 'v0.0.3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('function_auth_groups_group_id_fkey', 'function_auth_groups', type_='foreignkey')
    op.drop_column('function_auth_groups', 'group_id')
    op.add_column('function_auth_groups', Column('group_id', String(38)))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('function_auth_groups', 'group_id')
    op.add_column('function_auth_groups', Column('group_id', sa.Integer(), nullable=True))
    op.create_foreign_key('function_auth_groups_group_id_fkey', 'function_auth_groups', 'auth_groups', ['group_id'], ['id'])
    # ### end Alembic commands ###
