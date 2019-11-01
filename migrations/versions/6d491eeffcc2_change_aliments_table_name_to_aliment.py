"""change aliments table name to Aliment

Revision ID: 6d491eeffcc2
Revises: 90a70ff6d6a6
Create Date: 2019-10-31 10:36:46.486082

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d491eeffcc2'
down_revision = '90a70ff6d6a6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('aliment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('aliment_name', sa.String(length=140), nullable=True),
    sa.Column('description', sa.String(length=140), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('aliments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('aliments',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('aliment_name', sa.VARCHAR(length=140), nullable=True),
    sa.Column('description', sa.VARCHAR(length=140), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('aliment')
    # ### end Alembic commands ###