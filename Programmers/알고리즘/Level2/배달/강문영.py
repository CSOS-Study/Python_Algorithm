import heapq
import sys


def extract_weight(road):
    graph = {}

    for road_weight in road:
        town = str(road_weight[0])
        linked_town = str(road_weight[1])
        weight = road_weight[2]

        if not graph.get(town):
            graph[town] = {}
            graph[town][linked_town] = weight

        else:
            if not graph[town].get(linked_town):
                graph[town][linked_town] = weight
            elif graph[town][linked_town] > weight:
                graph[town][linked_town] = weight

        if not graph.get(linked_town):
            graph[linked_town] = {}
            graph[linked_town][town] = weight

        else:
            if not graph[linked_town].get(town):
                graph[linked_town][town] = weight
            elif graph[linked_town][town] > weight:
                graph[linked_town][town] = weight

    return graph


def solution(N, road, K):
    graph = extract_weight(road)
    distances = {node: sys.maxsize for node in graph}
    distances["1"] = 0
    queue = []
    heapq.heappush(queue, (distances["1"], "1"))

    while queue:
        current_distance, node = heapq.heappop(queue)
        if distances[node] < current_distance:
            continue

        for neighbor_node, neighbor_distance in graph[node].items():
            weight_distance = neighbor_distance + current_distance
            if weight_distance < distances[neighbor_node]:
                distances[neighbor_node] = weight_distance
                heapq.heappush(queue, (weight_distance, neighbor_node))

    result = list(filter(lambda x: x[1] <= K, distances.items()))

    return len(result)
