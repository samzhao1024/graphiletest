
from faker import Faker

from db import cursor, conn
from table import create_table_automotiveoem, create_table_models

fake = Faker()


def insert_companies():
    for i in range(26):
        sql = """
        insert into automotiveoem (company_name) values('{}');
        """.format(fake.company())
        cursor.execute(sql)
        conn.commit()


def insert_model():
    sql = """select id from automotiveoem"""
    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.commit()
    for row in rows:
        for i in range(1,10):
            sql = """insert into models (model_name, oem_id) values('{}', {});""".format(str(i), row[0])
            cursor.execute(sql)
            conn.commit()


if __name__ == '__main__':
    # create_table_automotiveoem()
    # insert_companies()
    create_table_automotiveoem()
    create_table_models()
    insert_companies()
    insert_model()


