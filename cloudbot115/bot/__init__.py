# -*- coding: utf-8 -*-
'''
Created on 2014/03/06

@author: deadblue
'''

from bot import handler
import webapp2

app = webapp2.WSGIApplication([
                               (r'/bot/starter', handler.StarterHandler),
                               (r'/bot/worker', handler.WorkerHandler)
                               ], debug=True)