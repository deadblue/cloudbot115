# -*- coding: utf-8 -*-
'''
Created on 2014/03/06

@author: deadblue
'''
import codecs
import json
import logging

def json_parse(s):
    obj = {}
    try:
        if s[:3] == codecs.BOM_UTF8:
            s = s.decode('utf-8-sig')
        obj = json.loads(s)
    except: 
        logging.error('parse failed: %s' % s)
    return obj