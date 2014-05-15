# -*- coding: utf-8 -*-
'''
Created on 2014/03/06

@author: deadblue
'''

import template

if __name__ == '__main__':
    print template.render('hello.html', {'name':'world'})