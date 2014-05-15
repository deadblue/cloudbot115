# -*- coding: utf-8 -*-
'''
Created on 2014/03/07

@author: deadblue
'''

from google.appengine.api import users
import json
import template

def output_html(tpl_name):
    '''
    输出装饰器，表示以html输出，需要传入模板名称
    '''
    def wrapper_creator(func):
        def wrapper(*args):
            try:
                result = apply(func, args)
                html = template.render(tpl_name, result)
                resp = args[0].response
                resp.headers['Content-Type'] = 'text/html; charset=utf8'
                resp.write(html)
            except AccessDeniedException:
                args[0].redirect(users.create_login_url(args[0].request.uri))
        return wrapper
    return wrapper_creator

def output_json(func):
    '''
    输出装饰器，表示以json输出
    '''
    def wrapper(*args):
        try:
            result = apply(func, args)
            resp = args[0].response
            resp.headers['Content-Type'] = 'application/json'
            json.dump(result, resp)
        except AccessDeniedException:
            pass
    return wrapper

def access_admin_only(func):
    '''
    表示仅允许管理员使用
    应放在输出装饰器下方（优先于输出装饰器执行）
    '''
    def wrapper(*args):
        if not users.is_current_user_admin():
            raise AccessDeniedException()
        else:
            return apply(func, args)
    return wrapper

class AccessDeniedException(Exception):
    pass