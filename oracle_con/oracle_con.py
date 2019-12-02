import cx_Oracle
import os
import time
from tqdm import * 

user_name = "TEST"

con = cx_Oracle.connect('admin/84218421@52.14.136.177/orcl')
curs = con.cursor()
print (con.version)

def create_user():
    file = open(os.path.join(os.path.dirname(__file__), 'ot_create_user.sql'), 'rt')   
    data = file.read()
    data = data.replace('OT', user_name)
    sql_commands = data.replace('\n', '').split(';')[:-1]
    file.close()

    for sql_command in tqdm(sql_commands):
        curs.execute(sql_command)

def create_tables():
    file = open(os.path.join(os.path.dirname(__file__), 'ot_schema.sql'), 'rt')      
    data = file.read()
    data = data.replace('OT.', user_name + '.')
    sql_commands = data.replace('\n', '').split(';')[:-1]
    file.close()

    for sql_command in tqdm(sql_commands):
        curs.execute(sql_command)

def insert_values():
    file = open(os.path.join(os.path.dirname(__file__), 'ot_data.sql'), 'rt')      
    data = file.read()
    data = data.replace('OT.', user_name + '.')
    sql_commands = data.replace('\n', '').split(';')[:-1]
    file.close()

    for sql_command in tqdm(sql_commands):
        curs.execute(sql_command)

create_user()
create_tables()
insert_values()
con.close()

























