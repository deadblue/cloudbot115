# -*- coding: utf-8 -*-
'''
Created on 2014/03/06

@author: deadblue
'''

import binascii
import hashlib
import random
import re
import time
import urllib
import urllib2
import util

__all__ = ['Client', 'LoginException', 'CheckinException']

class Client():

    def __init__(self, account, password):
        self._url_opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        self._login(account, password)
    def _login(self, account, password):
        vcode = _create_uniqid()
        query = {
              'login[safe]' : 1,
              'login[safe_login]' : 0,
              'login[ssoent]' : 'A1',
              'login[ssoext]' : vcode,
              'login[ssoln]' : account,
              'login[ssopw]' : _sha1_password(account, password, vcode),
              'login[ssovcode]' : vcode,
              'login[time]' : 1,
              'login[version]' : '2.0',
              'goto' : 'http://115.com/'
              }
        # 执行登陆请求
        login_url = 'http://passport.115.com/?ct=login&ac=ajax&is_ssl=1'
        resp = self._url_opener.open(login_url, urllib.urlencode(query))
        result = util.json_parse(resp.read())
        if result['state'] == False:
            raise LoginException()

    def checkin(self):
        token = self._get_checkin_token()
        if len(token.strip()) > 0:
            checkin_url = 'http://115.com/?ct=ajax_user&ac=checkin'
            resp = self._url_opener.open(checkin_url, urllib.urlencode({'token' : token}))
            result = util.json_parse(resp.read())
            return result['state']
        else:
            return False
    def _get_checkin_token(self):
        token_url = 'http://115.com/?ct=event&ac=get_active_param&_=%d' % (time.time() * 1000)
        resp = self._url_opener.open(token_url)
        result = util.json_parse(resp.read())
        token = result['is_take_token'] if result['state'] else ''
        return token
    
    def pick_spaces(self):
        token = self._get_take_token()
        picked_size = 0
        if len(token.strip()) > 0:
            pick_url = 'http://115.com/?ct=ajax_user&ac=pick_spaces&u=1&token=%s' % token
            resp = self._url_opener.open(pick_url)
            result = util.json_parse(resp.read())
            picked_size = result['picked_num'] if result['state'] else 0
        return picked_size
    def _get_take_token(self):
        page_url = 'http://115.com/?ct=yao'
        body = self._url_opener.open(page_url).read()
        m = re.search("var take_token = '(\w*)'", body, re.M|re.S)
        token = m.group(1)
        return token

class LoginException(Exception):
    pass
class CheckinException(Exception):
    pass

def _create_uniqid():
    def format_seed(seed, width):
        seed = '%x' % (seed)
        if len(seed) > width:
            seed = seed[0:width]
        else:
            seed = '0' * (width - len(seed)) + seed
        return seed
    php_js_seed = int(random.random() * 0x75bcd15)
    unique_id = '%s%s' % (format_seed(time.time(), 8), format_seed(php_js_seed, 5))
    return unique_id
def _sha1_password(account, password, vcode):
    def sha1_str(text):
        return binascii.b2a_hex( hashlib.sha1(text).digest() )
    return sha1_str( sha1_str( sha1_str(password) + sha1_str(account) ) + vcode.upper() )