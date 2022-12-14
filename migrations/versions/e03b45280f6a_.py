"""empty message

Revision ID: e03b45280f6a
Revises: f49583972f1c
Create Date: 2022-09-28 16:33:33.915101

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e03b45280f6a'
down_revision = 'f49583972f1c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('agent', sa.Column('created_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('agent', 'created_at')
    # ### end Alembic commands ###
