"""Remove password and add admin boolean to users table

Revision ID: 7c4f2ba2cb60
Revises: 6b0f2b119737
Create Date: 2023-12-14 13:37:09.701650

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '7c4f2ba2cb60'
down_revision: Union[str, None] = '6b0f2b119737'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('admin', sa.Boolean(), nullable=True))
    op.drop_column('users', 'password')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', mysql.VARCHAR(length=50), nullable=False))
    op.drop_column('users', 'admin')
    # ### end Alembic commands ###