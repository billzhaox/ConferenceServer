from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
introduction = Table('introduction', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('conference_id', INTEGER),
    Column('url', VARCHAR(length=128)),
)

Enroll = Table('Enroll', post_meta,
    Column('User_id', Integer),
    Column('Conference_id', Integer),
)

administrator = Table('administrator', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('username', String(length=64)),
    Column('email', String(length=120)),
    Column('password', String(length=64)),
)

conference = Table('conference', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('admin_id', Integer),
    Column('name', String(length=64)),
    Column('date', DateTime),
    Column('place', String(length=64)),
    Column('time', Time),
    Column('status', String(length=16)),
    Column('introduction', String(length=1024)),
    Column('guest_intro', String(length=1024)),
    Column('remark', String(length=128)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['introduction'].drop()
    post_meta.tables['Enroll'].create()
    post_meta.tables['administrator'].create()
    post_meta.tables['conference'].columns['admin_id'].create()
    post_meta.tables['conference'].columns['guest_intro'].create()
    post_meta.tables['conference'].columns['introduction'].create()
    post_meta.tables['conference'].columns['remark'].create()
    post_meta.tables['conference'].columns['status'].create()
    post_meta.tables['conference'].columns['time'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['introduction'].create()
    post_meta.tables['Enroll'].drop()
    post_meta.tables['administrator'].drop()
    post_meta.tables['conference'].columns['admin_id'].drop()
    post_meta.tables['conference'].columns['guest_intro'].drop()
    post_meta.tables['conference'].columns['introduction'].drop()
    post_meta.tables['conference'].columns['remark'].drop()
    post_meta.tables['conference'].columns['status'].drop()
    post_meta.tables['conference'].columns['time'].drop()
