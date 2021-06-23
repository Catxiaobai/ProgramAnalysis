#! /usr/bin/python3
# -*-coding:utf-8-*-

"""
@Time: 2021/6/22 10:51
@Author : mengjie-1998@qq.com
@Remark: a brief description
"""
from CFG.DrawGraph import *
from CFG.DuPath import *
from CFG.FindDU import *
from CFG.LexicalAnalysis import *
from CFG.SemanticAnalysis import *
from CFG.SourceProgram import *

if __name__ == '__main__':
    path = 'example/'
    name = 'prime'
    name2 = 'test'
    name3 = 'collatz'
    list_program = read_program(path, name)
    words_dict = parse_words(list_program)
    nodes, edges = divide_block(MAIN, words_dict, FUNCTION_DICT)
    draw_nodes = {}
    for key in nodes:
        draw_nodes[key] = list_program[key - 1]
    draw(draw_nodes, edges)
    print(words_dict)
    find_defines(draw_nodes)
    # find_uses(nodes)
    find_uses(draw_nodes, FUNCTION_DICT)
    du_path('i', DEFINES, USES, nodes, edges)
