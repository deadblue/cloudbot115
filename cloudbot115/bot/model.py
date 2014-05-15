# -*- coding: utf-8 -*-
'''
Created on 2014/03/07

@author: deadblue
'''

from google.appengine.ext import db

class Account(db.Model):
    account = db.StringProperty()
    password = db.StringProperty()
    status = db.IntegerProperty()
    last_active_time = db.DateTimeProperty()

class PickRecord(db.Model):
    account = db.StringProperty()
    pick_size = db.IntegerProperty()
    pick_time = db.DateTimeProperty()