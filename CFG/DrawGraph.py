#! /usr/bin/python3
# -*-coding:utf-8-*-

"""
@Time: 2021/6/22 20:14
@Author : mengjie-1998@qq.com
@Remark: a brief description
"""
from graphviz import Digraph


def draw(nodes, edges):
    graph = Digraph("CFG", 'comment', None, None, 'png', None, "UTF-8",
                    {'rankdir': 'TB'},
                    {'color': 'black', 'fontcolor': 'black',
                     'style': 'rounded',
                     'shape': 'box'},
                    {'color': '#999999', 'fontcolor': '#888888', 'fontsize': '10', 'fontname': 'FangSong'}, None, False)

    for key, value in nodes.items():
        graph.node(str(key), str(value))
    for edge in edges:
        edge_instance = edge.split(',')
        if edge_instance[0] != '0':
            graph.edge(edge_instance[0], edge_instance[-1])
    graph.view()
