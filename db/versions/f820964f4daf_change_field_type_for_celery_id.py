"""

Revision ID: f820964f4daf
Revises: 110d33875ca8
Create Date: 2024-01-03 09:00:15.759158

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'f820964f4daf'
down_revision: Union[str, None] = '110d33875ca8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('uploads', 'fastqc_process_id',
               existing_type=mysql.INTEGER(display_width=11),
               type_=sa.String(length=255),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('uploads', 'fastqc_process_id',
               existing_type=sa.String(length=255),
               type_=mysql.INTEGER(display_width=11),
               existing_nullable=True)
    # ### end Alembic commands ###
