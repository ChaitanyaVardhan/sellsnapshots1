from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
migration_tmp = Table('migration_tmp', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('firstname', VARCHAR(length=64)),
    Column('lastname', VARCHAR(length=64)),
    Column('city', VARCHAR(length=64)),
    Column('country', VARCHAR(length=64)),
    Column('email', VARCHAR(length=120)),
    Column('password_hash', VARCHAR(length=128)),
    Column('confirmed', BOOLEAN),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('firstname', String(length=64)),
    Column('lastname', String(length=64)),
    Column('city', String(length=64)),
    Column('country', String(length=64)),
    Column('email', String(length=120)),
    Column('password_hash', String(length=128)),
    Column('confirmed', Boolean, default=ColumnDefault(False)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['migration_tmp'].drop()
    post_meta.tables['user'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['migration_tmp'].create()
    post_meta.tables['user'].drop()
