# Created by CS Jackie - 
# https://www.youtube.com/watch?v=niB1tTeC2yI
# This is a sample Python script

from dijkstra import dijkstra

if __name__ == '__main__':
    print(f"Getting sample graph")
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'C': 3, 'D': 2, 'E': 3},
        'C': {'B': 1, 'D': 4, 'E': 5},
        'D': {},
        'E': {'D': 1}
    }
    print(graph)
    print(dijkstra(graph, 'A'))