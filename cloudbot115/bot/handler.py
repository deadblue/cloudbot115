# -*- coding: utf-8 -*-
'''
Created on 2014/03/06

@author: deadblue
'''

from bot import model, u115
from google.appengine.api import taskqueue
import datetime
import webapp2

class StarterHandler(webapp2.RequestHandler):

    def get(self):
        self.post()

    def post(self):
        query = model.Account.gql('WHERE status=0')
        for acnt in query:
            account = acnt.account
            taskqueue.add(queue_name='workqueue', url='/bot/worker', method='GET', 
                          params={'account' : account})

class WorkerHandler(webapp2.RequestHandler):

    def get(self):
        account = self.request.get('account')
        acnt = model.Account.get_by_key_name(account)
        if acnt is not None:
            try:
                now = datetime.datetime.now()
                # 执行任务
                client = u115.Client(acnt.account, acnt.password)
                client.checkin()
                pick_size = client.pick_spaces()
                acnt.last_active_time = now
                # 若成功领取，则记录
                if pick_size > 0:
                    record = model.PickRecord()
                    record.account = acnt.account
                    record.pick_size = pick_size
                    record.pick_time = now
                    record.save()
            except u115.LoginException:
                acnt.status = 2
            acnt.save()
