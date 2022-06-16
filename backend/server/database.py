from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import json
from os.path import expanduser

local_config = expanduser("~/etc/riselift_config.json")
launch_config = expanduser("~/etc/riselift_config.json")

with open(local_config) as config_file:
    config = json.load(config_file)

SQLALCHEMY_DATABASE_URL = 'postgresql://%s:%s@%s/%s' % (config.get("SQL_USER"), config.get("SQL_PASSWORD"), config.get("SQL_HOST"), config.get("SQL_DB"))

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal =  sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
