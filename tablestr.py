from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from faker import Faker

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/sqltest2")
Base = declarative_base()


class AutomotiveOEM(Base):
    __tablename__ = 'automotiveoem'
    id = Column(Integer, primary_key=True,autoincrement=True)
    company_name = Column(String, nullable=False, unique=True)

class Models(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True, autoincrement=True)
    model_name=Column(String,nullable=False)
    oem_id = Column(Integer, ForeignKey('automotiveoem.id'))



DBSession=sessionmaker(bind=engine)
fake = Faker()

def create_table():
    Base.metadata.create_all(engine)

def insert_companies():
    session=DBSession()
    for i in range(26):
        new_company=AutomotiveOEM(company_name=fake.company())
        session.add(new_company)
    session.commit()
    session.close()

def insert_models():
    session=DBSession()
    companies=session.query(AutomotiveOEM).all()
    for item in companies:
        for i in range(1, 10):
            new_model=Models(model_name=str(i),oem_id=item.id)
            session.add(new_model)
    session.commit()
    session.close()


#create_table()
#insert_companies()
#insert_models()



