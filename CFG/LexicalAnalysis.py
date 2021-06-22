#! /usr/bin/python3
# -*-coding:utf-8-*-

"""
@Time: 2021/6/22 11:59
@Author : mengjie-1998@qq.com
@Remark: a brief description
"""
import re

WORD = ['#define', 'fscanf', 'printf', 'long', 'int', 'void', 'float', 'double', 'char', 'short', 'struct', 'default',
        'return', 'const', 'static', 'if', 'else', 'switch', 'case', 'for', 'do', 'while', 'goto', 'continue', 'break']

TYPE_WORD = ['long', 'short', 'int', 'char', 'float', 'double', 'auto', 'void']

FUNCTION_DICT = {}  # 记录函数
VARIABLE_DICT = {}  # 记录变量
MAIN = []  # 记录main函数包含内容


# 拆分成词
def parse_words(raw_list):
    words_dict = {}
    for i in range(len(raw_list)):
        list_line = re.findall(r'#define|\w+|\W', raw_list[i])
        res = [x for x in list_line if x != ' ']
        # print(res)
        words_dict[i + 1] = res
    # print(words_dict)
    lexical_analysis(words_dict)
    return words_dict


# if-else硬解
def lexical_analysis(words_dict):
    for index, value in words_dict.items():
        # print(index, value)
        if value[0] == '#define':
            if value[1] not in TYPE_WORD:
                FUNCTION_DICT[value[1]] = value[2:]
        elif value[0] in TYPE_WORD:
            i = 0
            while i < len(value):
                if value[i] not in TYPE_WORD:
                    if re.match(r'[a-zA-Z_]+', value[i]):
                        if value[i + 1] == '(':
                            if value[i] == 'main':
                                FUNCTION_DICT[value[i]] = index
                            else:
                                FUNCTION_DICT[value[i]] = value[i + 1:]
                        VARIABLE_DICT[value[i]] = ''
                i = i + 1
    # print(FUNCTION_DICT)
    # print(VARIABLE_DICT)
    get_main(words_dict)
    return FUNCTION_DICT, VARIABLE_DICT


def get_main(words_dict):
    stack = []
    for i in range(FUNCTION_DICT['main'] + 1, len(words_dict) + 1):
        # print(i)
        # print(words_dict[i])
        if words_dict[i][0] == '{':
            stack.append('{')
        elif words_dict[i][0] == '}':
            stack.pop()
            if len(stack) == 0:
                MAIN.append(i)
        if len(stack) > 0:
            MAIN.append(i)
    return MAIN
