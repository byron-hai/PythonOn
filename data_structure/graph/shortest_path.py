#!/usr/bin/env python3
"""
@ Desc:
  In python, a dict can represent a graph. each node is a key,
  and the connected nodes are its values
@ Author: Byron
@ Date: 
"""


def search_graph(graph,  start, end):
    results = []
    generate_path(graph, [start], end, results)

    results.sort(key=lambda x: len(x))
    return results


def generate_path(graph, path, end, results):
    state = path[-1]
    if state == end:
        results.append(path)
    else:
        for node in graph[state]:
            if node not in path:
                generate_path(graph, path + [node], end, results)


if __name__ == "__main__":
    graph = {'A': ['B', 'C', 'D'],
             'B': ['E'],
             'C': ['D', 'F'],
             'D': ['B', 'E', 'G'],
             'E': [],
             'F': ['D', 'G'],
             'G': ['E']}

    r1 = search_graph(graph, 'A', 'F')
    #print('A -> F: ', ' -> '.join(r1))
    print(r1)
    r2 = search_graph(graph, 'A', 'G')
    for r in r2:
        print('A -> G: ', ' -> '.join(r))
