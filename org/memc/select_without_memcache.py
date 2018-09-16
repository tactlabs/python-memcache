#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on Mar 14, 2018

Course work: 

@author: raja

Source:
    http://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/
    http://www.sqlitetutorial.net/sqlite-python/insert/
    
    https://docs.python.org/3/library/sqlite3.html
    https://stackoverflow.com/questions/7831371/is-there-a-way-to-get-a-list-of-column-names-in-sqlite
    https://stackoverflow.com/questions/228912/sqlite-parameter-substitution-problem
    
    Create table
        http://www.sqlitetutorial.net/sqlite-python/create-tables/
    
    Date format readable:
        https://stackoverflow.com/questions/2158347/how-do-i-turn-a-python-datetime-into-a-string-with-readable-format-date
        
    Geo Location
        http://en.mygeoposition.com/        
    
    DB:
    tasks:
        id, name, priority
    projects:
        id, name, begin_date, end_date
'''

# Import necessary modules
import sqlite3
from sqlite3 import Error
from random import randint
from datetime import datetime 
 
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None


def select_all_from_table(conn, table):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM "+table)
 
    rows = cur.fetchall()
    
    print('rows : '+str(len(rows)))
    
    if(len(rows) <= 0):
        print('No Data available');
 
    for row in rows:
        print(row) 
 
def main():
    database = "pythonsqlite.db"
 
    # create a database connection
    conn = create_connection(database)
    
    with conn:
        
        select_all_from_table(conn, 'projects')
 
 
if __name__ == '__main__':
    main()