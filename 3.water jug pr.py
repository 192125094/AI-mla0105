from collections import deque

def pour(jug, max_capacity):
    return max(0, min(jug[0] + jug[1], max_capacity))

def water_jug_problem(capacity_x, capacity_y, target):
    visited_states = set()
    queue = deque([(0, 0, [])])

    while queue:
        current_state = queue.popleft()
        current_x, current_y, path = current_state

        if current_x == target or current_y == target:
            print("Solution found:")
            for step in path:
                print(step)
            return

        visited_states.add((current_x, current_y))

        # Fill jug X
        fill_x = (capacity_x, current_y, path + [f"Fill jug X: {capacity_x}"])
        if fill_x[:2] not in visited_states:
            queue.append(fill_x)

        # Fill jug Y
        fill_y = (current_x, capacity_y, path + [f"Fill jug Y: {capacity_y}"])
        if fill_y[:2] not in visited_states:
            queue.append(fill_y)

        # Empty jug X
        empty_x = (0, current_y, path + ["Empty jug X"])
        if empty_x[:2] not in visited_states:
            queue.append(empty_x)

        # Empty jug Y
        empty_y = (current_x, 0, path + ["Empty jug Y"])
        if empty_y[:2] not in visited_states:
            queue.append(empty_y)

        # Pour water from jug X to jug Y
        pour_xy = (max(0, current_x - (capacity_y - current_y)), pour((current_x, current_y), capacity_y),
                   path + ["Pour X to Y"])
        if pour_xy[:2] not in visited_states:
            queue.append(pour_xy)

        # Pour water from jug Y to jug X
        pour_yx = (pour((current_x, current_y), capacity_x), max(0, current_y - (capacity_x - current_x)),
                   path + ["Pour Y to X"])
        if pour_yx[:2] not in visited_states:
            queue.append(pour_yx)

    print("No solution found.")

if __name__ == "__main__":
    capacity_x = 4
    capacity_y = 3
    target = 2

    water_jug_problem(capacity_x, capacity_y, target)
