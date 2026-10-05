# Lab 4: Informed Search: Heuristics & A*
# File Name: lab4_astar_audit.py

import heapq

# Campus Graph Adjacency List: (neighbor, weight)
graph = {
    'S': [('A', 1), ('B', 4)],
    'A': [('C', 2)],
    'B': [('G', 5)],
    'C': [('G', 3)],
    'G': []
}

# Standard Admissible & Consistent Heuristic
h_standard = {
    'S': 5,
    'A': 4,
    'B': 4,
    'C': 2,
    'G': 0
}

# Overestimating (Inadmissible) Heuristic for Task 3
h_overestimate = {
    'S': 5,
    'A': 4,
    'B': 4,
    'C': 10,  # Deliberate overestimate (true remaining cost is 3)
    'G': 0
}

# Zero Heuristic for UCS Control Run
h_zero = {
    'S': 0, 'A': 0, 'B': 0, 'C': 0, 'G': 0
}

def run_search(graph, h_dict, start='S', goal='G'):
    # Priority Queue elements: (f_score, g_score, current_node, path)
    pq = [(h_dict[start], 0, start, [start])]
    best_g = {start: 0}
    expanded_nodes = []
    
    while pq:
        f, g, node, path = heapq.heappop(pq)
        
        # Skip stale queue entries
        if g > best_g.get(node, float('inf')):
            continue
            
        expanded_nodes.append((node, g, h_dict[node], f))
        
        if node == goal:
            return path, g, expanded_nodes
            
        for nxt, weight in graph.get(node, []):
            ng = g + weight
            if ng < best_g.get(nxt, float('inf')):
                best_g[nxt] = ng
                nf = ng + h_dict[nxt]
                heapq.heappush(pq, (nf, ng, nxt, path + [nxt]))
                
    return None, float('inf'), expanded_nodes

if __name__ == "__main__":
    print("=" * 65)
    print("        LAB 4: INFORMED SEARCH (A* vs UCS) AUDIT TRACE")
    print("=" * 65)
    
    # Task 2 Run 1: Standard A* Search
    a_path, a_cost, a_trace = run_search(graph, h_standard)
    print("\n[1] Standard A* Search Execution:")
    print(f"    Returned Path   : {' -> '.join(a_path)}")
    print(f"    Total Path Cost : {a_cost}")
    print(f"    Expanded Count  : {len(a_trace)}")
    print("    Expansion Trace (Node, g, h, f):")
    for item in a_trace:
        print(f"      Node {item[0]}: g={item[1]}, h={item[2]}, f={item[3]}")

    # Task 2 Run 2: Zero-Heuristic (UCS Control)
    u_path, u_cost, u_trace = run_search(graph, h_zero)
    print("\n[2] UCS (Zero Heuristic) Execution:")
    print(f"    Returned Path   : {' -> '.join(u_path)}")
    print(f"    Total Path Cost : {u_cost}")
    print(f"    Expanded Count  : {len(u_trace)}")
    print("    Expansion Trace (Node, g, h, f):")
    for item in u_trace:
        print(f"      Node {item[0]}: g={item[1]}, h={item[2]}, f={item[3]}")

    # Task 3 Run: Overestimated Heuristic [h(C) = 10]
    o_path, o_cost, o_trace = run_search(graph, h_overestimate)
    print("\n[3] Overestimated A* Search [h(C)=10]:")
    print(f"    Returned Path   : {' -> '.join(o_path)}")
    print(f"    Total Path Cost : {o_cost}")
    print(f"    Expanded Count  : {len(o_trace)}")
    print("    Expansion Trace (Node, g, h, f):")
    for item in o_trace:
        print(f"      Node {item[0]}: g={item[1]}, h={item[2]}, f={item[3]}")
    print("=" * 65)