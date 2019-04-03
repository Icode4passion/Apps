"""empty message

Revision ID: 74524cd225d3
Revises: 
Create Date: 2018-12-03 19:48:16.258365

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74524cd225d3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bucketlist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_modified', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bucketlist')
    # ### end Alembic commands ###