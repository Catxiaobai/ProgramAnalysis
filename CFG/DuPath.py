#! /usr/bin/python3
# -*-coding:utf-8-*-

"""
@Time: 2021/6/23 3:42
@Author : mengjie-1998@qq.com
@Remark: a brief description
"""

MATRIX = {}
FLAG = {}
BRANCH = {}
INDEX = []
PATH = []
FULL_PATH = []
DU_PATH = {}


def all_path(nodes, edges):
    for edge in edges:
        edge_instance = edge.split(',')
        if edge_instance[0] != '0':
            if edge_instance[0] in MATRIX.keys():
                MATRIX[edge_instance[0]].append(edge_instance[-1])
            else:
                MATRIX[edge_instance[0]] = [edge_instance[-1]]

    DFS(nodes)
    return MATRIX


def DFS(nodes):
    for key in nodes:
        FLAG[str(key)] = 0
    a = list(FLAG.keys())[0]
    PATH.append(a)
    FLAG[a] = FLAG[a] + 1
    b = MATRIX.get(a)
    end = 1
    while end:
        end = 0
        for i in FLAG:
            if FLAG[i] == 0:
                end = 1
        if b is None:
            # PATH.append(a)
            pass
        elif len(b) == 1:
            a = b[0]
            PATH.append(a)
            if FLAG[a] == 0:
                FLAG[a] = FLAG[a] + 1

            else:
                k = INDEX[-1]
                if BRANCH[k] < len(MATRIX[k]):
                    a = k
                    PATH.append('/')
                    PATH.append(a)
                else:
                    pass
        elif len(b) > 1:
            if BRANCH.get(a) is None:
                INDEX.append(a)
                BRANCH[a] = 0
                a = b[BRANCH[a]]
                PATH.append(a)
                FLAG[a] = FLAG[a] + 1
            elif BRANCH[a] < len(b) - 1:
                BRANCH[a] = BRANCH[a] + 1
                a = b[BRANCH[a]]
                PATH.append(a)
                FLAG[a] = FLAG[a] + 1
            else:
                INDEX.pop()
                a = INDEX[-1]
                PATH.append('/')
                PATH.append(a)
        b = MATRIX.get(a)
        # print(FLAG)
        # print(PATH)
    temp = []
    i = 0
    while i < len(PATH):
        if PATH[i] == '/':
            while i + 2 < len(PATH) and PATH[i + 2] == '/':
                i = i + 2
            else:
                temp.append(PATH[i])
        else:
            temp.append(PATH[i])
        i = i + 1
    PATH.clear()

    new_path = []
    for i in temp:
        if i != '/':
            new_path.append(i)
        else:
            PATH.append(new_path)
            new_path = []
    PATH.append(new_path)
    new_path = PATH

    format_path()


def du_path(variable, defines, uses, nodes, edges):
    all_path(nodes, edges)
    # print(variable)
    # print('def', defines)
    # print('use', uses)
    for i in defines[variable]:
        for j in uses[variable]:
            find_du(str(i), str(j))
    print('变量'+variable+'的du_path:')
    for key in DU_PATH:
        print(key, DU_PATH[key])
    # print(DU_PATH)
    # print(variable, defines, uses, nodes, edges)


def find_du(src, tar):
    for i in FULL_PATH:
        if src in i and tar in i:
            p = []
            # print(i.index(src))
            ii = i[i.index(src):]
            # print(i)
            # print(ii)
            if tar in ii:
                # print(ii.index(tar))
                iii = ii[:ii.index(tar) + 1]
                p = iii
            # print(src, '->', tar, ':', p)
            DU_PATH[src+'->'+tar] = p

    return DU_PATH

def format_path():
    # print(PATH)
    FULL_PATH.append(PATH[0])
    for i in range(1, len(PATH)):
        j = len(FULL_PATH)
        while j:
            # print(j)
            j = j - 1
            if PATH[i][0] in FULL_PATH[j]:
                index = FULL_PATH[j].index(PATH[i][0])
                FULL_PATH.append(FULL_PATH[j][:index] + PATH[i])
    # print(FULL_PATH)
