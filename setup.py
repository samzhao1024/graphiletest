from sqlalchemy import Column, Integer, String, ForeignKey

from db import Base, engine, session


class AutomotiveOEM(Base):
    __tablename__ = 'automotiveoem'
    id = Column(Integer, primary_key=True,autoincrement=True)
    company_name = Column(String, nullable=False, unique=True)

    # def __repr__(self):
    #     tpl = "AutomotiveOEM(id={}, company_name={})"
    #     return tpl.format(self.id, self.company_name)


class Models(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True, autoincrement=True)
    model_name=Column(String,nullable=False)
    oem_id = Column(Integer, ForeignKey('automotiveoem.id'))


print("Start schema-setup stage")


try:
    Base.metadata.create_all(engine)
    session.close()
    print("Schema-setup stage sucessfully")
except Exception as e:
    print(e)
    session.close()


