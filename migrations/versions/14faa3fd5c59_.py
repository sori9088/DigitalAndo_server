"""empty message

Revision ID: 14faa3fd5c59
Revises: 
Create Date: 2020-01-11 17:23:07.791551

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14faa3fd5c59'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('issues',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('line_id', sa.String(length=256), nullable=True),
    sa.Column('issue_type', sa.String(length=256), nullable=True),
    sa.Column('detail1', sa.String(length=256), nullable=True),
    sa.Column('datail2', sa.String(length=256), nullable=True),
    sa.Column('remark', sa.Text(), nullable=True),
    sa.Column('status', sa.String(length=256), nullable=True),
    sa.Column('submit_date', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('start_date', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('finish_date', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('issues')
    # ### end Alembic commands ###
