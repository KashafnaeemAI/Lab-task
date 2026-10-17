import heapq

def astar(graph, h, start, goal):
    queue = [(h[start], 0, start, [start])]
    visited = set()
    
    while queue:
        f, g, node, path = heapq.heappop(queue)
        
        if node == goal:
            return g, path, list(visited)
            
        if node in visited:
            continue
        visited.add(node)
        
        for next_node, cost in graph[node].items():
            if next_node not in visited:
                new_g = g + cost
                new_f = new_g + h[next_node]
                heapq.heappush(queue, (new_f, new_g, next_node, path + [next_node]))
                
    return None, None, list(visited)

graph = {
    "S": {"A": 1, "B": 4},
    "A": {"C": 2},
    "B": {"G": 5},
    "C": {"G": 3},
    "G": {}
}

h_standard = {"S": 5, "A": 4, "B": 4, "C": 2, "G": 0}
h_overestimate = {"S": 5, "A": 4, "B": 4, "C": 10, "G": 0}

print("=== 1. A* Search (Standard) ===")
cost, path, visited = astar(graph, h_standard, "S", "G")
print(f"Path: {' -> '.join(path)}, Cost: {cost}, Visited: {visited}\n")

print("=== 2. UCS Search (Heuristic = 0) ===")
h_ucs = {"S": 0, "A": 0, "B": 0, "C": 0, "G": 0}
cost_ucs, path_ucs, visited_ucs = astar(graph, h_ucs, "S", "G")
print(f"Path: {' -> '.join(path_ucs)}, Cost: {cost_ucs}, Visited: {visited_ucs}\n")

print("=== 3. A* Search (Overestimated h(C) = 10) ===")
cost_over, path_over, visited_over = astar(graph, h_overestimate, "S", "G")
print(f"Path: {' -> '.join(path_over)}, Cost: {cost_over}, Visited: {visited_over}")