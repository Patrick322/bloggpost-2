"""adds category column to post

Revision ID: d7a32bf8291a
Revises: 1a4485bbb860
Create Date: 2019-10-27 17:08:20.241591

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd7a32bf8291a'
down_revision = '1a4485bbb860'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('category', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'category')
    # ### end Alembic commands ###
