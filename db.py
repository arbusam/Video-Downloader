import sqlite3
import time
import datetime
import random
from tabulate import tabulate

connection = sqlite3.connect("student.sqlite")
cur = connection.cursor()

# DB Functions

def create_table(tableName):
    sql = f"""
        CREATE TABLE IF NOT EXISTS {tableName} (
        id INT PRIMARY KEY AUTOINCREMENT,
        url VARCHAR,
        created_date REAL,
        download_date REAL );
    """
    cur.execute(sql)
    connection.commit()

def add_data(tableName, url):
    sql = f"INSERT INTO {tableName} (url, download_date) VALUES ({url}, {time.time()})"
    cur.execute(sql)
    connection.commit()

def read_from_table():
    sql = "SELECT * FROM students"
    cur.execute(sql)
    data = cur.fetchall()
    # print(data)
    # for row in data:
    #     print(row)
    return data

def get_column_names():
    sql = "SELECT * FROM students"
    cur.execute(sql)
    columns = cur.description
    return columns

def empty_table(tableName):
    sql = f"DELETE FROM {tableName}"
    cur.execute(sql)
    connection.commit()

def drop_table(tableName):
    sql = f"DROP TABLE {tableName}"
    cur.execute(sql)
    connection.commit()

def update_table():
    sql = ""
    cur.execute(sql)
    connection.commit()
