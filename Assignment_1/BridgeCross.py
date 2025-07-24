from collections import deque
from itertools import combinations

# Crossing times
times = {
    'Amogh': 5,
    'Ameya': 10,
    'Grandmother': 20,
    'Grandfather': 25
}

# Initial state: (left side, right side, umbrella side, time)
initial_state = (['Amogh', 'Ameya', 'Grandmother', 'Grandfather'], [], 'left', 0)

# Goal check
def is_goal(state):
    left, right, side, time_elapsed = state
    return len(left) == 0 and time_elapsed <= 60

# Successor function
def get_successors(state):
    left, right, umbrella, time_elapsed = state
    successors = []

    if umbrella == 'left':
        # Choose 2 people to go from left to right
        for pair in combinations(left, 2):
            new_left = left.copy()
            new_right = right.copy()
            for person in pair:
                new_left.remove(person)
                new_right.append(person)
            cost = max(times[pair[0]], times[pair[1]])
            new_state = (new_left, new_right, 'right', time_elapsed + cost)
            action = f"{pair[0]} and {pair[1]} cross → ({cost} min)"
            successors.append((new_state, action))
    else:
        # One person returns from right to left
        for person in right:
            new_right = right.copy()
            new_left = left.copy()
            new_right.remove(person)
            new_left.append(person)
            cost = times[person]
            new_state = (new_left, new_right, 'left', time_elapsed + cost)
            action = f"{person} returns ← ({cost} min)"
            successors.append((new_state, action))
    return successors

# BFS search
def bfs():
    queue = deque()
    queue.append((initial_state, []))
    visited = set()

    while queue:
        current_state, path = queue.popleft()
        left, right, umbrella, time_elapsed = current_state
        state_key = (tuple(sorted(left)), tuple(sorted(right)), umbrella)

        if state_key in visited or time_elapsed > 60:
            continue
        visited.add(state_key)

        if is_goal(current_state):
            return path + [(current_state, "Goal reached")]

        for next_state, action in get_successors(current_state):
            queue.append((next_state, path + [(current_state, action)]))
    return None

# DFS search
def dfs():
    stack = []
    stack.append((initial_state, []))
    visited = set()

    while stack:
        current_state, path = stack.pop()
        left, right, umbrella, time_elapsed = current_state
        state_key = (tuple(sorted(left)), tuple(sorted(right)), umbrella)

        if state_key in visited or time_elapsed > 60:
            continue
        visited.add(state_key)

        if is_goal(current_state):
            return path + [(current_state, "Goal reached")]

        for next_state, action in reversed(get_successors(current_state)):
            stack.append((next_state, path + [(current_state, action)]))
    return None

# Print path
def print_solution(path, method_name):
    print(f"\n{method_name} Solution ({path[-1][0][3]} minutes):\n")
    for i, (state, action) in enumerate(path):
        left, right, umbrella, time_elapsed = state
        print(f"Step {i}:")
        print(f"  Action: {action}")
        print(f"  Left: {left}, Right: {right}, Umbrella: {umbrella}, Time: {time_elapsed} min\n")

# Main
if __name__ == "__main__":
    print("Solving Bridge Problem with BFS and DFS...\n")

    bfs_path = bfs()
    if bfs_path:
        print_solution(bfs_path, "BFS")
    else:
        print("No BFS solution found within 60 minutes.")

    dfs_path = dfs()
    if dfs_path:
        print_solution(dfs_path, "DFS")
    else:
        print("No DFS solution found within 60 minutes.")
