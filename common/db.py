import sqlite3
import time
import datetime
import random
from tabulate import tabulate
from colorama import init, Fore, Back, Style
from .config import *
from .language_en import *

connection = sqlite3.connect(db_name)
cur = connection.cursor()

# DB Functions

def create_table(tableName):
    sql = f"""
            CREATE TABLE IF NOT EXISTS {tableName} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url VARCHAR,
            type TEXT,
            created_date REAL,
            download_date REAL );
           """
    cur.execute(sql)
    connection.commit()

# def insert_one_row(tableName, url, types):
#     sql = f"INSERT INTO {tableName} (url, created_date, download_date) VALUES ('{url}', '{types}' {time.time()}, {time.time()})"
#     cur.execute(sql)
#     connection.commit()

def add_data(db_table, tbl_fields, tbl_values):
    url_list = tbl_values[0]
    download_type = tbl_values[1]

    for link in url_list:
        sql = f"""
                INSERT INTO {db_table}
                ({tbl_fields})
                VALUES
                ("{link}", "{download_type}", "{time.time()}")
            """
        try:
            cur.execute(sql)
            connection.commit()
        except sqlite3.IntegrityError as e:
            print(SKIPPED_LINK_NAME.format(url=link))
        else:
            print(ADDED_LINK_NAME.format(url=link))

def read_from_table(db_table, where_expr):
    sql = f"""
            SELECT * 
            FROM {db_table}
            {where_expr}
           """
    cur.execute(sql)
    data = cur.fetchall()

    return data

def update_download_date(db_table, id):
    sql = f"UPDATE {db_table} SET download_date = {time.time()} WHERE id = {id}"
    cur.execute(sql)
    connection.commit()

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