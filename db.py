from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

pgsql = {
    "host": "",
    "port": "",
    "user": "",
    "password": "",
    "database": ""
}

print("Connect to the PostgreSQL database")

for key in pgsql.keys():
    print("Enter PostgreSQL {}".format(key.capitalize()))
    pgsql[key] = input()


try:
    engine = create_engine(
        "postgresql+psycopg2://{}:{}@{}:{}/{}".format(
            pgsql["user"],
            pgsql["password"],
            pgsql["host"],
            pgsql["port"],
            pgsql["database"],
            echo=True))
    Session = sessionmaker(bind=engine)
    session = Session()
    Base = declarative_base()
except Exception as e:
    print(e)
    exit()
