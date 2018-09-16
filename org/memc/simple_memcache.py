#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on May 17, 2018

@author: raja.raman

Source:
    https://realpython.com/python-memcache-efficient-caching/
'''

from pymemcache.client import base

def main():    
    
    client = base.Client(('localhost', 11211))
    
    client.set('some_key', 'some value')
    
    key = client.get('some_key').decode('utf-8')
    
    print(key)

if __name__ == '__main__':
    main()