"""remove table posts, add relationship between User and aliments

Revision ID: 90a70ff6d6a6
Revises: 64024b33ad87
Create Date: 2019-10-30 11:22:47.566787

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90a70ff6d6a6'
down_revision = '64024b33ad87'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_post_timestamp', table_name='post')
    op.drop_table('post')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('body', sa.VARCHAR(length=140), nullable=True),
    sa.Column('timestamp', sa.DATETIME(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_post_timestamp', 'post', ['timestamp'], unique=False)
    # ### end Alembic commands ###
