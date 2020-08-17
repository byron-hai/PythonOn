#!/usr/bin/env python3
"""
@ Desc: 
@ Author: Byron
@ Date: 
"""
from collections import deque


def find_shortest_path(path_map, start, end):
    checked_nodes = []
    search_queue = deque()
    search_queue.extend(path_map[start])
    path = []

    while search_queue:
        next_node = search_queue.popleft()
        if end in path_map[next_node]:
            path += [next_node, end]
            return path
        else:
            path.append(next_node)
            if next_node not in checked_nodes:
                search_queue.extend(path_map[next_node])
                checked_nodes.append(next_node)
    return False


if __name__ == "__main__":
    path_map = {'cab': ['car', 'cat'],
                'car': ['cat', 'bar'],
                'cat': ['mat', 'bat'],
                'bar': ['bat'],
                'mat': ['bat'],
                'bat': ['bat']}

    start, end = "cab", "bat"
    shortest_path = find_shortest_path(path_map, start, end)
    if shortest_path:
        print("PATH: " + " --> ".join(shortest_path))
    else:
        print("No path")

    path_map_b = {'a': ['b', 'c'],
                  'b': ['d', 'e'],
                  'c': ['d'],
                  'd': ['e', 'g'],
                  'e': ['h', 'f'],
                  'f': ['g'],
                  'g': ['h'],
                  'h': ['h']}
    start_b, end_b = 'a', 'h'
    shortest_path = find_shortest_path(path_map_b, start_b, end_b)
    if shortest_path:
        print("PATH: " + " --> ".join(shortest_path))
    else:
        print("No path")
