#! /usr/bin/python3
# -*-coding:utf-8-*-

"""
@Time: 2021/6/23 2:06
@Author : mengjie-1998@qq.com
@Remark: a brief description
"""
import re

DEFINES = {}
USES = {}


def find_defines(nodes):
    for key in nodes:
        # print(key, nodes[key])
        if len(re.findall(r'=', nodes[key])) == 1:
            variable = nodes[key].split('=')[0].split('[')
            variable[0] = variable[0].strip()
            if variable[0] in DEFINES.keys():
                DEFINES[variable[0]].append(key)
            else:
                DEFINES[variable[0]] = [key]
            USES[variable[0]] = []
    for key in DEFINES:
        DEFINES[key] = sorted(DEFINES[key])
    # print(DEFINES)
    return DEFINES


def find_uses(nodes, function_dict):
    # print(USES)
    for key in nodes:
        # print(key, nodes[key])
        # print(re.findall(r'\+|-|\*|/|==', nodes[key]))
        if len(re.findall(r'=', nodes[key])) == 1:
            # print(nodes[key].replace(' ', '').split('=', 1)[-1])
            res = nodes[key].split('=', 1)[-1]
            # print(res)
            # print(re.findall(r'\W|\w+', res))
            for r in re.findall(r'\W|\w+', res):
                if r in DEFINES.keys():
                    USES[r].append(key)
        elif len(re.findall(r'\+|-|\*|/|==|>|<|%|!', nodes[key])):
            # print(nodes[key])
            # print(re.findall(r'\W|\w+', nodes[key]))
            res = re.findall(r'#define|\w+|\W', nodes[key])
            res = [x for x in res if x != ' ']
            # print(res)
            for r in res:
                if r in USES.keys():
                    # print(r, key)
                    USES[r].append(key)
                    USES[r] = list(set(USES[r]))
        else:
            # print(nodes[key])
            res = re.findall(r'#define|\w+|\W', nodes[key])
            res = [x for x in res if x != ' ']
            # print(list(set(function_dict) & set(res)))
            if list(set(function_dict) & set(res)):
                for r in res:
                    if r in USES.keys():
                        # print(r, key)
                        USES[r].append(key)
                        USES[r] = list(set(USES[r]))
    for key in USES:
        USES[key] = sorted(USES[key])
    # print(USES)
    return USES
