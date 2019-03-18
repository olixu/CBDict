#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    CBDict

    A tool to translate English to Chinese.

    date: 18/03/2019
    author: oliverxu
    homepage: https://blog.oliverxu.cn
    license: MIT
    copyright: Copyright (c) 2019 oliverxu. All rights reserved
"""

import sys
import json
import re
import requests
import pyperclip
import time

__name__ = "CBDict"
__version__ = "0.0.1"
__description__ = "This program monitors the clipboard of the system and translate the word from English to Chinese by YouDao api, especially designed for Students who are working under linux environment where there is no simple translater when you reading papers."
__keywords__ = "Translation English2Chinese ClipBoard"
__author__ = "oliverxu"
__contact__ = "273601727@qq.com"
__url__ = "https://blog.oliverxu.cn"
__license__ = "MIT"

class Dict:
    key = '716426270'
    keyFrom = 'wufeifei'
    api = 'http://fanyi.youdao.com/openapi.do' \
          '?keyfrom=wufeifei&key=716426270&type=data&doctype=json&version=1.1&q='
    content = None

    def __init__(self, word):
        if len(word) > 0:
            self.api = self.api + word
            self.translate()
        else:
            print('取词错误')

    def translate(self):
        try:
            content = requests.get(self.api).content
            self.content = json.loads(content.decode('utf-8'))
            self.parse()
        except Exception as e:
            print('错误：无法访问远程服务器!')
            print(e)

    def parse(self):
        code = self.content['errorCode']
        if code == 0:  # Success
            c = None
            try:
                u = self.content['basic']['us-phonetic']  # English
                e = self.content['basic']['uk-phonetic']
            except KeyError:
                try:
                    c = self.content['basic']['phonetic']  # Chinese
                except KeyError:
                    c = 'None'
                u = 'None'
                e = 'None'

            try:
                explains = self.content['basic']['explains']
            except KeyError:
                explains = 'None'

            try:
                phrase = self.content['web']
            except KeyError:
                phrase = 'None'

            print('\033[1;31m################################### \033[0m')
            print('\033[1;31m# \033[0m {0} {1}'.format(
                self.content['query'], self.content['translation'][0]))
            if u != 'None':
                print('\033[1;31m# \033[0m (U: {0} E: {1})'.format(u, e))
            elif c != 'None':
                print('\033[1;31m# \033[0m (Pinyin: {0})'.format(c))
            else:
                print('\033[1;31m# \033[0m')

            print('\033[1;31m# \033[0m')

            if explains != 'None':
                for i in range(0, len(explains)):
                    print('\033[1;31m# \033[0m {0}'.format(explains[i]))
            else:
                print('\033[1;31m# \033[0m Explains None')

            print('\033[1;31m# \033[0m')

            if phrase != 'None':
                for p in phrase:
                    print('\033[1;31m# \033[0m {0} : {1}'.format(
                        p['key'], p['value'][0]))
                    if len(p['value']) > 0:
                        if re.match('[ \u4e00 -\u9fa5]+', p['key']) is None:
                            blank = len(p['key'].encode('gbk'))
                        else:
                            blank = len(p['key'])
                        for i in p['value'][1:]:
                            print('\033[1;31m# \033[0m {0} {1}'.format(
                                ' ' * (blank + 3), i))

            print('\033[1;31m################################### \033[0m')
            # Phrase
            # for i in range(0, len(self.content['web'])):
            #     print self.content['web'][i]['key'], ':'
            #     for j in range(0, len(self.content['web'][i]['value'])):
            #         print self.content['web'][i]['value'][j]
        elif code == 20:  # Text to long
            print('WORD TO LONG')
        elif code == 30:  # Trans error
            print('TRANSLATE ERROR')
        elif code == 40:  # Don't support this language
            print('CAN\'T SUPPORT THIS LANGUAGE')
        elif code == 50:  # Key failed
            print('KEY FAILED')
        elif code == 60:  # Don't have this word
            print('DO\'T HAVE THIS WORD')

def main():
    oldword = ''

    while(True):
        time.sleep(1)
        word = pyperclip.paste()
        if len(word)>0 and word != oldword:
            Dict(pyperclip.paste())
            oldword = word

if __name__ == '__main__':
    main()