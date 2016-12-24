"""empty message

Revision ID: 8e00515e684c
Revises: 
Create Date: 2016-12-20 21:27:28.354417

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e00515e684c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('games',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('winner', sa.Enum('white', 'black', name='color'), nullable=True),
    sa.Column('handicap', sa.SmallInteger(), nullable=True),
    sa.Column('komi', sa.SmallInteger(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('players',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=30), nullable=True),
    sa.Column('last_name', sa.String(length=30), nullable=True),
    sa.Column('aga_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_players_aga_id'), 'players', ['aga_id'], unique=True)
    op.create_table('black_player_games',
    sa.Column('player_id', sa.Integer(), nullable=False),
    sa.Column('game_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['game_id'], ['games.id'], ),
    sa.ForeignKeyConstraint(['player_id'], ['players.id'], ),
    sa.PrimaryKeyConstraint('player_id', 'game_id')
    )
    op.create_table('white_player_games',
    sa.Column('player_id', sa.Integer(), nullable=False),
    sa.Column('game_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['game_id'], ['games.id'], ),
    sa.ForeignKeyConstraint(['player_id'], ['players.id'], ),
    sa.PrimaryKeyConstraint('player_id', 'game_id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('white_player_games')
    op.drop_table('black_player_games')
    op.drop_index(op.f('ix_players_aga_id'), table_name='players')
    op.drop_table('players')
    op.drop_table('games')
    ### end Alembic commands ###