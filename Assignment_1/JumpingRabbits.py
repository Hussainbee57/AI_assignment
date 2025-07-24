from collections import deque

# Initial and Goal States
initial_state = ['E', 'E', 'E', '_', 'W', 'W', 'W']
goal_state =    ['W', 'W', 'W', '_', 'E', 'E', 'E']

# Function to check valid moves
def is_valid_move(state, i, j):
    if j < 0 or j >= len(state):
        return False
    if state[i] == '_' or state[j] != '_':
        return False
    if abs(i - j) == 1:  # step
        return True
    elif abs(i - j) == 2:  # jump
        middle = (i + j) // 2
        if state[middle] != '_' and state[middle] != state[i]:  # jump over opposite rabbit
            return True
    return False

# Generate valid neighbors
def get_neighbors(state):
    neighbors = []
    for i in range(len(state)):
        for d in [-2, -1, 1, 2]:
            j = i + d
            if is_valid_move(state, i, j):
                new_state = state[:]
                new_state[i], new_state[j] = new_state[j], new_state[i]
                neighbors.append(new_state)
    return neighbors

# BFS Search
def bfs(start, goal):
    queue = deque([(start, [start])])
    visited = set()
    while queue:
        current, path = queue.popleft()
        if current == goal:
            return path
        visited.add(tuple(current))
        for neighbor in get_neighbors(current):
            if tuple(neighbor) not in visited:
                queue.append((neighbor, path + [neighbor]))
    return None

# DFS Search
def dfs(start, goal):
    stack = [(start, [start])]
    visited = set()
    while stack:
        current, path = stack.pop()
        if current == goal:
            return path
        visited.add(tuple(current))
        for neighbor in get_neighbors(current):
            if tuple(neighbor) not in visited:
                stack.append((neighbor, path + [neighbor]))
    return None

# Function to print solution path
def print_path(path, method_name):
    print(f"\n{method_name} Solution ({len(path) - 1} moves):\n")
    for step, state in enumerate(path):
        print(f"Step {step}: {''.join(state)}")

# Main function
if __name__ == "__main__":
    print("Solving Rabbit Leap Problem...\n")

    # BFS
    bfs_solution = bfs(initial_state, goal_state)
    if bfs_solution:
        print_path(bfs_solution, "BFS")
    else:
        print("No solution found using BFS.")

    # DFS
    dfs_solution = dfs(initial_state, goal_state)
    if dfs_solution:
        print_path(dfs_solution, "DFS")
    else:
        print("No solution found using DFS.")
