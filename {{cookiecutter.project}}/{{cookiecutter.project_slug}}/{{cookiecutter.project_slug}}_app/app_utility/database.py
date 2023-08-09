from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

POSTGRES_USER=os.getenv('POSTGRES_USER','POSTGRES_USER_NOT_PROVIDED')
POSTGRES_PW=os.getenv('POSTGRES_PW','POSTGRES_PW_NOT_PROVIDED')
POSTGRES_HOST=os.getenv('POSTGRES_HOST','POSTGRES_HOST_NOT_PROVIDED')
POSTGRES_PORT=os.getenv('POSTGRES_PORT','POSTGRES_PORT_NOT_PROVIDED')
POSTGRES_DB=os.getenv('POSTGRES_DB','POSTGRES_DB_NOT_PROVIDED')

SQLALCHEMY_DATABASE_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PW}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
sessionlocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)

Base = declarative_base()