# -*- coding: utf-8 -*-
'''
Created on 2014/03/07

@author: deadblue
'''

from bot import model
from page import decorator
import webapp2

class IndexHandler(webapp2.RequestHandler):

    @decorator.output_html('main.html')
    @decorator.access_admin_only
    def get(self):
        acnts = model.Account.all()
        return {'content' : 'index.html', 'accounts' : acnts}

class AccountHandler(webapp2.RequestHandler):

    @decorator.output_html('account.html')
    @decorator.access_admin_only
    def get(self):
        acnts = model.Account.all()
        return {'accounts' : acnts}

class RecordHandler(webapp2.RequestHandler):

    @decorator.output_html('main.html')
    def get(self):
        return {'content' : 'record.html'}

class AjaxAccountHandler(webapp2.RequestHandler):

    @decorator.output_json
    def post(self):
        action = self.request.get('action')
        account = self.request.get('account')
        password = self.request.get('password')
        acnt = model.Account.get_by_key_name(account)
        if action == 'insert':
            acnt = model.Account(key_name=account)
            acnt.account = account
            acnt.password = password
            acnt.status = 0
        elif action == 'update':
            acnt.password = password
        elif action == 'disable':
            acnt.status = 1
        elif action == 'enable':
            acnt.status = 0
        acnt.save()
        return {'error' : 0}

class TestHandler(webapp2.RequestHandler):

    @decorator.output_html('comment.html')
    def get(self):
        return {
                'content' : '这是回复',
                'user_name' : '这些都不重要',
                'post_time' : '不要在意细节',
                'quote' : [
                           { 'content' : '这是第1层' },
                           { 'content' : '这是第2层' },
                           { 'content' : '这是第3层' },
                           { 'content' : '这是第4层' },
                           { 'content' : '这是第5层' },
                           { 'content' : '这是第6层' },
                           ]
                }