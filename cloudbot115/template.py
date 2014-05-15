# -*- coding: utf-8 -*-
'''
Created on 2014/03/07

@author: deadblue
'''

from os import path
import jinja2

__engine__ = 'jinja2'

_TEMPLATE_ROOT = path.join(path.dirname(__file__), 'templates')

_JINJA2_ENV = jinja2.Environment(
                                loader=jinja2.FileSystemLoader(_TEMPLATE_ROOT),
                                extensions=['jinja2.ext.autoescape'],
                                autoescape=True
                                )

def render(tpl_name, data):
    if __engine__ == 'jinja2':
        return _jinja2_render(tpl_name, data)
    else:
        return None

def _jinja2_render(tpl_name, data):
    tpl = _JINJA2_ENV.get_template(tpl_name)
    return tpl.render(data)
