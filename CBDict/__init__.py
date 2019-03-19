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
import notify2

__name__ = "CBDict"
__version__ = "2.0"
__description__ = "This program monitors the clipboard of the system and translate the word from English to Chinese by YouDao api, especially designed for Students who are working under linux environment where there is no simple translater when you reading papers."
__keywords__ = "Translation English2Chinese ClipBoard"
__author__ = "oliverxu"
__contact__ = "273601727@qq.com"
__url__ = "https://blog.oliverxu.cn"
__license__ = "MIT"

def print_note(note):
    notify2.init('CBDict')
    n = notify2.Notification(note)
    n.show()

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
            print_note('取词错误')

    def translate(self):
        try:
            content = requests.get(self.api).content
            self.content = json.loads(content.decode('utf-8'))
            self.parse()
        except Exception as e:
            print_note('错误：无法访问远程服务器!')
            print_note(e)

    def parse(self):
        outcome = ''
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

            outcome = outcome + self.content['query'] + ' ' + self.content['translation'][0] + '\n'
            if u != 'None':
                outcome = outcome + 'U:' + u + 'E:' + e + '\n'
            elif c != 'None':
                outcome = outcome + 'Pinyin:' + c + '\n'
            else:
                outcome = outcome + '\n'

            if explains != 'None':
                for i in range(0, len(explains)):
                    outcome = outcome + explains[i] + '\n'
                    #print(explains)
            else:
                outcome = outcome + '无法找到解释' + '\n'

            if phrase != 'None':
                for p in phrase:
                    value = ''
                    for i in p['value']:
                        value = value + i + ' '
                    outcome = outcome + p['key'] + ' : ' + value + '\n'
            print_note(outcome)
            print(outcome)
            print('\033[1;31m################################### \033[0m')

        elif code == 20:  # Text to long
            print_note('输入单词太长')
        elif code == 30:  # Trans error
            print_note('翻译错误')
        elif code == 40:  # Don't support this language
            print_note('不支持这种语言')
        elif code == 50:  # Key failed
            print_note('密钥错误')
        elif code == 60:  # Don't have this word
            print_note('没有这个单词')

def main():
    oldword = ''
    pyperclip.copy('')
    print_note('CBDict词典已经开启，你复制了什么就能翻译什么' + '\n' + '项目主页：https://blog.oliverxu.cn')
    while(True):
        time.sleep(1)
        word = pyperclip.paste()
        if len(word)>0 and word != oldword:
            Dict(word)
            oldword = word

if __name__ == '__main__':
    main()