"""Added column to user model

Revision ID: 15af3105196f
Revises: 07b01599374d
Create Date: 2022-07-30 14:35:08.842675

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15af3105196f'
down_revision = '07b01599374d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'created_at')
    # ### end Alembic commands ###
