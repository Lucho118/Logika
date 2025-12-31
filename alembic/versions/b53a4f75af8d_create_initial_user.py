"""create initial user

Revision ID: b53a4f75af8d
Revises: 0f0a7fd46eea
Create Date: 2025-12-30 19:34:32.950046

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from app.core.security import hash_password


# revision identifiers, used by Alembic.
revision: str = 'b53a4f75af8d'
down_revision: Union[str, Sequence[str], None] = '0f0a7fd46eea'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    users_table = sa.table(
        "users",
        sa.column("id", sa.Integer),
        sa.column("email", sa.String),
        sa.column("hashed_password", sa.String),
        sa.column("is_active", sa.Integer),
    )

    op.bulk_insert(
        users_table,
        [
            {
                "email": "admin@example.com",
                "hashed_password": "$2b$12$E1nKqPz/XBvH.BU5Y8uHMuRZzwrG4ZOwiB2Jcc/Hqg71ACCTHNReC",
                "is_active": 1,
            }
        ],
    )


def downgrade() -> None:
    """Downgrade schema."""
    pass
