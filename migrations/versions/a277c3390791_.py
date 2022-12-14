"""empty message

Revision ID: a277c3390791
Revises: 8b4bdecc2b0f
Create Date: 2022-09-28 11:37:25.792116

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a277c3390791'
down_revision = '8b4bdecc2b0f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('agent',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fullname', sa.String(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('country', sa.String(), nullable=True),
    sa.Column('PhoneNumber', sa.Integer(), nullable=True),
    sa.Column('linkedin', sa.String(), nullable=True),
    sa.Column('Email', sa.String(), nullable=True),
    sa.Column('profilePic', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('properties', sa.Column('agent_id', sa.Integer(), nullable=True))
    op.drop_constraint('properties_user_id_fkey', 'properties', type_='foreignkey')
    op.create_foreign_key(None, 'properties', 'agent', ['agent_id'], ['id'])
    op.drop_column('properties', 'user_id')
    op.drop_column('users', 'country')
    op.drop_column('users', 'PhoneNumber')
    op.drop_column('users', 'fullname')
    op.drop_column('users', 'profilePic')
    op.drop_column('users', 'linkedin')
    op.drop_column('users', 'address')
    op.alter_column('wish_list', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('wish_list', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.add_column('users', sa.Column('address', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('linkedin', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('profilePic', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('fullname', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('PhoneNumber', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('country', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('properties', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'properties', type_='foreignkey')
    op.create_foreign_key('properties_user_id_fkey', 'properties', 'users', ['user_id'], ['id'])
    op.drop_column('properties', 'agent_id')
    op.drop_table('agent')
    # ### end Alembic commands ###
