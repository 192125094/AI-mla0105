from collections import deque

def print_state(state):
    for row in state:
        print(row)
    print()

def get_blank_position(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_neighbors(state):
    blank_row, blank_col = get_blank_position(state)
    neighbors = []

    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Possible moves: right, down, left, up

    for move in moves:
        new_row, new_col = blank_row + move[0], blank_col + move[1]

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = [row.copy() for row in state]
            new_state[blank_row][blank_col], new_state[new_row][new_col] = new_state[new_row][new_col], 0
            neighbors.append(new_state)

    return neighbors

def solve_8_puzzle(initial_state, goal_state):
    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        current_state, path = queue.popleft()

        if current_state == goal_state:
            print("Solution found!")
            print("Number of steps:", len(path))
            return path

        visited.add(tuple(map(tuple, current_state)))

        for neighbor in get_neighbors(current_state):
            if tuple(map(tuple, neighbor)) not in visited:
                queue.append((neighbor, path + [neighbor]))

    print("No solution found.")
    return None

if __name__ == "__main__":
    initial_state = [
        [1, 2, 3],
        [4, 0, 5],
        [6, 7, 8]
    ]

    goal_state = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    solution_path = solve_8_puzzle(initial_state, goal_state)

    if solution_path:
        for step, state in enumerate(solution_path):
            print(f"Step {step + 1}:")
            print_state(state)
    else:
        print("No solution found.")
