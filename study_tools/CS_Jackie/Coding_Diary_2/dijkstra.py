# need to learn about heapq (min heaps)
import heapq

def dijkstra(graph, start_node):
    print('Start running the nodes')
    visited_nodes = set()
    distances = {start_node: 0}
    priority_queue = [(0, start_node)]

    while priority_queue:
        (weight, node) = heapq.heappop(priority_queue)
        
        if node not in visited_nodes:
            visited_nodes.add(node)
            for neighbor, distance in graph[node].items():
                if neighbor not in distances or distances[node] + distance < distances[neighbor]:
                    distances[neighbor] = distances[node] + distance
                    heapq.heappush(priority_queue, (distances[neighbor], neighbor))

    print('Finished')
    return distances 
