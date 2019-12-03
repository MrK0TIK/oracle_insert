import cx_Oracle
import os
import time
from tqdm import * 

user_name = "TEST"

con = cx_Oracle.connect('admin/84218421@52.14.136.177/orcl')
curs = con.cursor()

def create_user():
    file = open(os.path.join(os.path.dirname(__file__), 'ot_create_user.sql'), 'rt')   
    data = file.read()
    data = data.replace('OT', user_name)
    sql_commands = data.replace('\n', '').split(';')[:-1]
    file.close()
    try:
        for sql_command in tqdm(sql_commands):
            curs.execute(sql_command)
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        if error.code == 1920:
            print ('Schema already exists continue creating tables in existing schema: ' + user_name)

def create_tables():
    file = open(os.path.join(os.path.dirname(__file__), 'ot_schema.sql'), 'rt')      
    data = file.read()
    data = data.replace('OT.', user_name + '.')
    sql_commands = data.replace('\n', '').split(';')[:-1]
    file.close()
    try:
        for sql_command in tqdm(sql_commands):
            curs.execute(sql_command)
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        if error.code == 955:
            print('Tables already exists')

def insert_values():
    file = open(os.path.join(os.path.dirname(__file__), 'ot_data.sql'), 'rt')      
    data = file.read()
    data = data.replace('OT.', user_name + '.')
    sql_commands = data.split(';')[:-1]
    file.close()
    try:
        for sql_command in tqdm(sql_commands):
            curs.execute(sql_command)
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        if error.code == 942:
            print('Table does not exist')
        elif error.code == 1:
            print('Unique constraint violated')

def drop_tables():
    file = open(os.path.join(os.path.dirname(__file__), 'ot_drop.sql'), 'rt')
    data = file.read()
    data = data.replace('OT.', user_name + '.')
    sql_commands = data.split(';')[:-1]
    file.close()
    try:
        for sql_command in tqdm(sql_commands):
            curs.execute(sql_command)
        print('Tables deleted')    
    except cx_Oracle.DatabaseError as e:
       error, = e.args
       if error.code == 942:
           print('There is nothing to drop')

if __name__ == "__main__":
    create_user()
    create_tables()
    insert_values()
    con.close()

























