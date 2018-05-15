from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
introduction = Table('introduction', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('path', VARCHAR(length=128)),
    Column('conference_id', INTEGER),
)

introduction = Table('introduction', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('url', String(length=128)),
    Column('conference_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['introduction'].columns['path'].drop()
    post_meta.tables['introduction'].columns['url'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['introduction'].columns['path'].create()
    post_meta.tables['introduction'].columns['url'].drop()
