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
from pymemcache.client import base
 
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
    
    print('selecting from DB')
    
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
        print('No Data available')
        return None
 
    '''
    for row in rows:
        print(row)
    '''
    
    return rows
        
def get_data_from_db():
    database = "pythonsqlite.db"
 
    # create a database connection
    conn = create_connection(database)
    
    with conn:        
        result = select_all_from_table(conn, 'projects')        
        print(result)
        
        return result 
 
def main():
    
    client = base.Client(('localhost', 11211))
    
    result = client.get('my_projects')
    
    #client.delete('my_projects')
    #return
    
    if(result is None):
        result_db = get_data_from_db()
        client.set('my_projects', result_db)
        return
    
    print(result)
    return
 
if __name__ == '__main__':
    main()
    
    
'''
More:

https://stackoverflow.com/questions/606191/convert-bytes-to-a-string

https://stackoverflow.com/questions/868690/good-examples-of-python-memcache-memcached-being-used-in-python

https://stackoverflow.com/questions/11943591/invalidating-cache-based-on-version-using-memcached
'''