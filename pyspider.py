#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2024-06-13 14:02:15
# Project: test

from pyspider.libs.base_handler import *
from bs4 import BeautifulSoup
import requests

def extract_token(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find('input', {'name': 'csrf_token'})['value']

class Handler(BaseHandler):

    crawl_config = {}

    @every(minutes=24 * 60)
    def on_start(self):
        
        url = 'http://192.168.1.156:8069/web/login'
        s = requests.Session()
        # 先GET登录页面
        login_page = s.get(url)

        # 从返回的HTML中提取token
        token = extract_token(login_page.text)

        # 提交表单
        form_data = {
            'login': '1',
            'password': '1',
            'csrf_token': token   # 添加token到表单数据
        }

        res = s.post(url, data=form_data)

        print(res)
