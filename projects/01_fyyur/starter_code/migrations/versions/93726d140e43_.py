"""empty message

Revision ID: 93726d140e43
Revises: 
Create Date: 2020-12-10 20:25:24.517514

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '93726d140e43'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('showListings',
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('venue_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['Artist.id'], ),
    sa.ForeignKeyConstraint(['venue_id'], ['Venue.id'], ),
    sa.PrimaryKeyConstraint('artist_id', 'venue_id')
    )
    op.drop_column('Venue', 'start_time')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('start_time', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.drop_table('showListings')
    # ### end Alembic commands ###
