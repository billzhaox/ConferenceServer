from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
conference = Table('conference', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64)),
    Column('date', DateTime),
    Column('place', String(length=64)),
)

introduction = Table('introduction', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('path', String(length=128)),
    Column('conference_id', Integer),
)

user = Table('user', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('nickname', VARCHAR(length=64)),
    Column('email', VARCHAR(length=120)),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('username', String(length=64)),
    Column('email', String(length=120)),
    Column('password', String(length=64)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['conference'].create()
    post_meta.tables['introduction'].create()
    pre_meta.tables['user'].columns['nickname'].drop()
    post_meta.tables['user'].columns['password'].create()
    post_meta.tables['user'].columns['username'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['conference'].drop()
    post_meta.tables['introduction'].drop()
    pre_meta.tables['user'].columns['nickname'].create()
    post_meta.tables['user'].columns['password'].drop()
    post_meta.tables['user'].columns['username'].drop()
