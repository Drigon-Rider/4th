inputGraph = {
    'A': [('B', 5), ('D', 12)],
    'B': [('A', 9), ('C', 4)],
    'C': [('D', 4), ('B', 7)],
    'D': [('A', 9), ('C', 5)]
}

goal = "D"

def gbfs(graph, start):
    queue = [start]  # Initialize the queue with the start node
    visitedNode = []  # Initialize a list to keep track of visited nodes

    while queue:
        queue = sorted(queue, key=lambda x: x[1])  # Sort the queue based on the heuristic function
        node, _ = queue.pop(0)  # Pop the node with the lowest heuristic value

        if node not in visitedNode:
            visitedNode.append(node)  # Mark the node as visited

            if node == goal:  # If the goal node is reached, exit the loop
                break

            neighbours = graph[node]  # Get the neighbours of the current node

            for neighbour, cost in neighbours:
                queue.append((neighbour, cost))  # Add neighbours to the queue
                
    return visitedNode  # Return the list of visited nodes

def calculate_path_cost(visited_nodes):
    path_cost = 0
    for i in range(len(visited_nodes) - 1):
        current_node = visited_nodes[i]
        next_node = visited_nodes[i + 1]
        for neighbor, cost in inputGraph[current_node]:
            if neighbor == next_node:
                path_cost += cost  # Calculate the total path cost
                break
    return path_cost

result = gbfs(inputGraph, ("A", 0))  # Start with path_cost as 0
print("Visited Nodes:")
print(result)
print("Total Path Cost:", calculate_path_cost(result))
