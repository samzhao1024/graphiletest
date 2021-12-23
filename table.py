from db import cursor, conn


def create_table_automotiveoem():
    sql = """
    create table automotiveoem
(
id serial primary key not null,
company_name text
);
    """
    cursor.execute(sql)
    conn.commit()


def create_table_models():
    sql = """
    create table models
    (
id serial primary key not null,
model_name text,
oem_id int references automotiveoem(id)
);
    """
    cursor.execute(sql)
    conn.commit()