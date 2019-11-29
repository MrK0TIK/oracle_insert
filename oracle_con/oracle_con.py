import cx_Oracle
import os

con = cx_Oracle.connect('admin/84218421@52.14.136.177/orcl')
curs = con.cursor()
print (con.version)

file = open(os.path.join(os.path.dirname(__file__),'ot_create_user.sql'), 'r')
full_sql = file.read()
sql_commands = full_sql.split(';')

for sql_command in sql_commands:
    curs.execute(sql_command)

def create_tables():
    file = open(os.path.join(os.path.dirname(__file__),'ot_schema.sql'), 'r')
    full_sql = file.read()
    sql_commands = full_sql.split(';')

    for sql_command in sql_commands:
        curs.execute(sql_command)


def insert_values():
    file = open(os.path.join(os.path.dirname(__file__), 'ot_data.sql'), 'r')
    full_sql = file.read()
    sql_commands = full_sql.split(';')

    for sql_command in sql_commands:
        curs.execute(sql_command)
        print(sql_command)

create_tables()
insert_values()
con.close()

























