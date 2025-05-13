from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'sqlite:///./blog.db'
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine,autocommit=False,autoflush=False)

Base = declarative_base()

# create_engine = It creates a connection engine to the database (like a gate to access the database).
# declarative_base() = its is used to create a base class for your table models (not directly to create the table).
# sessionmaker = sessionmaker is used to create a Session class, which you then use to create session objects to communicate with the DB.
# 'sqlite:///./blog.db' = sqlite kuda connect panrathu and db file name
# connect_args={"check_same_thread": False} = fastapi muti thread but SQLite single thread so false kodukurom
# autocommit=False → You have to call commit() manually. Safer, gives control.
# autoflush=False → Changes are not automatically pushed to DB while querying; you control when to flush (send) data.
