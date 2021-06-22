#! /usr/bin/python3
# -*-coding:utf-8-*-

"""
@Time: 2021/6/22 16:38
@Author : mengjie-1998@qq.com
@Remark: a brief description
"""

NODE = {}
EDGE = []
BLOCK = {}
WHILE = {}
IF = {}
ELSE = {}
FOR = {}
ACTION = {}


# 切分成块
def divide_block(main, words_dict, function_dict):
    # print(main, words_dict)
    stack = []
    source = []
    target = 0
    out = 0
    # todo: 第一行不能是功能，必须是一个赋值语句
    # todo: 没有考虑for和else if
    for i in main:
        # print(i, words_dict[i])
        if words_dict[i][0] == '{':
            stack.append({'{': i})
            if len(stack) > 1:
                if ACTION[i - 1] != 'else':
                    source.append(source[-1])
        elif words_dict[i][0] == '}':

            if len(stack) > 1:
                for s in stack[-1].values():
                    pass
                stack.pop()
                if ACTION[s - 1] == 'if' or ACTION[s - 1] == 'else':
                    out = out + 1
                    fir = source[-1]
                    source.pop()
                    sec = source[-1]
                    source.pop()
                    source.append(fir)
                    source.append(sec)
                elif ACTION[s - 1] == 'while':
                    EDGE.append(str(source[-1]) + ',' + str(source[-2]))
                    source.pop()

        elif words_dict[i][0] == 'for':
            ACTION[i] = 'for'
            NODE[i] = words_dict[i]
            NODE[i] = words_dict[i]
            out = out + 1
            while out:
                out = out - 1
                target = i
                EDGE.append(str(source[-1]) + ',' + str(target))
                source.pop()
            source.append(target)

        elif words_dict[i][0] == 'if':
            ACTION[i] = 'if'
            NODE[i] = words_dict[i]
            out = out + 1
            while out:
                out = out - 1
                target = i
                EDGE.append(str(source[-1]) + ',' + str(target))
                source.pop()
            source.append(target)
        elif words_dict[i][0] == 'else':
            ACTION[i] = 'else'
            out = out - 1
        elif words_dict[i][0] == 'while':
            ACTION[i] = 'while'
            NODE[i] = words_dict[i]
            out = out + 1
            while out:
                out = out - 1
                target = i
                EDGE.append(str(source[-1]) + ',' + str(target))
                source.pop()
            source.append(target)
        elif words_dict[i][0] in function_dict:
            NODE[i] = words_dict[i]
            out = out + 1
            while out:
                out = out - 1
                target = i
                EDGE.append(str(source[-1]) + ',' + str(target))
                source.pop()
            source.append(target)
        else:
            NODE[i] = words_dict[i]
            out = out + 1
            if len(source) == 0:
                out = out - 1
                target = i
                EDGE.append('0' + ',' + str(target))
                source.append(target)
            else:
                while out:
                    out = out - 1
                    target = i
                    EDGE.append(str(source[-1]) + ',' + str(target))
                    source.pop()
                source.append(target)

    return NODE, EDGE
