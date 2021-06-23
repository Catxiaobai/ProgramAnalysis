#! /usr/bin/python3
# -*-coding:utf-8-*-

"""
@Time: 2021/6/22 10:40
@Author : mengjie-1998@qq.com
@Remark: a brief description
"""

import re


# 读取源文件并写入同名txt文件中
def read_program(filepath, filename):
    list_program = []
    pat = r'#include.*'
    with open(filepath + filename + '.c', 'r', encoding='utf-8') as f:
        for line in f:
            if line != '\n' and re.match(pat, line) is None:
                line = line.strip('\n').strip()
                # print(line)
                if len(line) > 1:
                    if line[0] == '{' or line[0] == '}':
                        list_program.append(line[0])
                        if line[-1] == '{' or line[-1] == '}':
                            list_program.append(line[1:-1].strip('\n').strip())
                            list_program.append(line[-1])
                        else:
                            list_program.append(line[1:].strip('\n').strip())
                    elif line[-1] == '{' or line[-1] == '}':
                        list_program.append(line[:-1].strip('\n').strip())
                        list_program.append(line[-1])
                    elif '{' in line:
                        print('waring:', '源文件存在未处理的{符号')
                        list_program.append(line)
                    else:
                        list_program.append(line)
                else:
                    list_program.append(line)
    # print(list_program)
    with open(filepath + filename + '.txt', 'w', encoding='utf-8') as f:
        for line in list_program:
            f.write(line + '\n')
    return list_program


