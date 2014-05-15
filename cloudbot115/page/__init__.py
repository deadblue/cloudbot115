# -*- coding: utf-8 -*-
'''
Created on 2014/03/06

@author: deadblue
'''

from page import handler
import webapp2

app = webapp2.WSGIApplication([
                               (r'/', handler.IndexHandler),
                               (r'/account', handler.AccountHandler),
                               (r'/record', handler.RecordHandler),
                               (r'/ajax/account', handler.AjaxAccountHandler),
                               (r'/test', handler.TestHandler)
                               ], debug=True)