"""empty message

Revision ID: f8c3c19678f4
Revises: 4432ecd5a563
Create Date: 2025-06-10 23:56:21.193739

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f8c3c19678f4'
down_revision = '4432ecd5a563'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Favorites', schema=None) as batch_op:
        batch_op.drop_constraint('Favorites_planet_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('Favorites_vehicle_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'Planet', ['planet_id'], ['id'])
        batch_op.create_foreign_key(None, 'Vehicle', ['vehicle_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Favorites', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('Favorites_vehicle_id_fkey', 'Person', ['vehicle_id'], ['id'])
        batch_op.create_foreign_key('Favorites_planet_id_fkey', 'Person', ['planet_id'], ['id'])

    # ### end Alembic commands ###
