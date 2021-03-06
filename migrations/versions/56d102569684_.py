"""empty message

Revision ID: 56d102569684
Revises: 6bcebbb3e042
Create Date: 2018-09-10 15:50:38.943071

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56d102569684'
down_revision = '6bcebbb3e042'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('is_draft', sa.BOOLEAN(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # ### end Alembic commands ###
    op.drop_column('post', 'is_draft')
