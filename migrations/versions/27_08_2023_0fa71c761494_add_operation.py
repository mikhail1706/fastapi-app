"""Add Operation

Revision ID: 0fa71c761494
Revises: 52230e3a1cab
Create Date: 2023-08-27 20:51:01.571399

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0fa71c761494'
down_revision: Union[str, None] = '52230e3a1cab'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('operation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.String(), nullable=True),
    sa.Column('figi', sa.String(), nullable=True),
    sa.Column('instrument_type', sa.String(), nullable=True),
    sa.Column('data', sa.TIMESTAMP(), nullable=True),
    sa.Column('type', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('operation')
    # ### end Alembic commands ###