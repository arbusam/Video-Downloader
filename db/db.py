import sqlite3
import time
import datetime
import random
from tabulate import tabulate
from colorama import init, Fore, Back, Style
from .config import *

connection = sqlite3.connect(db_name)
cur = connection.cursor()

# DB Functions

def create_table(tableName):
    sql = f"""
        CREATE TABLE IF NOT EXISTS {tableName} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        url VARCHAR,
        created_date REAL,
        download_date REAL );
    """
    cur.execute(sql)
    connection.commit()

def add_data(tableName, url):
    sql = f"INSERT INTO {tableName} (url, created_date, download_date) VALUES ('{url}', {time.time()}, {time.time()})"
    cur.execute(sql)
    connection.commit()

def read_from_table(table_name):
    sql = f"SELECT * FROM {table_name}"
    cur.execute(sql)
    data = cur.fetchall()
    return data

def get_column_names(tableName):
    sql = f"SELECT * FROM {tableName}"
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