"""new fields in user model

Revision ID: 042979116aaf
Revises: fe426ce64f0e
Create Date: 2018-11-14 14:42:31.072978

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '042979116aaf'
down_revision = 'fe426ce64f0e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
