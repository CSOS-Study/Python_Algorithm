import heapq
import sys

graph = {
    "A": {"B": 10, "C": 3},
    "B": {"C": 1, "D": 2},
    "C": {"B": 4, "D": 8, "E": 2},
    "D": {"E": 7},
    "E": {"D": 9}
}


def dijkstara(start):
    distances = {node: sys.maxsize for node in graph}
    distances[start] = 0
    queue = []

    heapq.heappush(queue, (distances[start], start))

    while queue:
        current_distance, node = heapq.heappop(queue)
        if distances[node] < current_distance:
            continue

        for neighbor_node, distance in graph[node].items():
            weighted_distance = current_distance + distance
            if weighted_distance < distances[neighbor_node]:
                distances[neighbor_node] = weighted_distance
                heapq.heappush(queue, (weighted_distance, neighbor_node))

    return distances

result = dijkstara("A")
