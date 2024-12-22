"""Add unique constraints to URL column

Revision ID: 84124552e8a8
Revises: 
Create Date: 2024-12-22 11:54:38.234483

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '84124552e8a8'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table('link_mappings') as batch_op:
        batch_op.create_unique_constraint(
            batch_op.f('uq_link_mappings_url'), ['url'])


def downgrade() -> None:
    with op.batch_alter_table('link_mappings') as batch_op:
        batch_op.drop_constraint(
            batch_op.f('uq_link_mappings_url'), type_='unique')
