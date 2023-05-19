"""empty message

Revision ID: 551eef68762b
Revises: f1c8ae857868
Create Date: 2023-05-17 17:50:29.110271

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '551eef68762b'
down_revision = 'f1c8ae857868'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('planet_name', sa.String(length=120), nullable=False),
    sa.Column('population', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('planet_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planet')
    # ### end Alembic commands ###
