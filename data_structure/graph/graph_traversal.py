#!/usr/bin/env python3
"""
@ Desc: 
@ Author: Byron
@ Date: 
"""
from collections import deque


def breadth_first_search(graph, root):
    visited_nodes = list()
    graph_queue = deque([root])

    while len(graph_queue) > 0:
        node = graph_queue.popleft()
        print(node)
        if node not in visited_nodes:
            visited_nodes.append(node)
            graph_queue.extend(graph[node])
        print(graph_queue)

    return visited_nodes


def depth_first_search(graph, root):
    visited_nodes = list()
    graph_stack = [root]

    while len(graph_stack) > 0:
        node = graph_stack.pop()
        if node not in visited_nodes:
            visited_nodes.append(node)
            graph_stack.extend(graph[node])

    return visited_nodes


if __name__ == "__main__":
    graph1 = dict()
    graph1['A'] = ['B', 'G', 'D']
    graph1['B'] = ['A', 'F', 'E']
    graph1['C'] = ['F', 'H']
    graph1['D'] = ['A', 'F']
    graph1['E'] = ['B', 'G']
    graph1['F'] = ['B', 'C', 'D']
    graph1['G'] = ['A', 'E']
    graph1['H'] = ['C']

    graph = dict()
    graph['A'] = ['B', 'S']
    graph['B'] = ['A']
    graph['S'] = ['A', 'G', 'C']
    graph['D'] = ['C']
    graph['G'] = ['S', 'F', 'H']
    graph['H'] = ['G', 'E']
    graph['E'] = ['C', 'H']
    graph['F'] = ['C', 'G']
    graph['C'] = ['D', 'S', 'E', 'F']
    print(breadth_first_search(graph, 'A'))
    print(depth_first_search(graph, 'A'))
