"""added email to user

Revision ID: 8053dfef68d8
Revises: f04210e0ad59
Create Date: 2019-10-22 15:32:24.137191

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8053dfef68d8'
down_revision = 'f04210e0ad59'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('email', sa.String(length=50), nullable=True))
    op.create_unique_constraint(None, 'user', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('user', 'email')
    # ### end Alembic commands ###
