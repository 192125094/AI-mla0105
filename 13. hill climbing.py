import random

def objective_function(solution):
    # Define the objective function to be optimized
    return sum(x**2 for x in solution)

def hill_climbing(initial_solution, step_size, max_iterations):
    current_solution = initial_solution
    current_value = objective_function(current_solution)

    for _ in range(max_iterations):
        # Generate a neighboring solution by perturbing the current solution
        neighbor_solution = [x + random.uniform(-step_size, step_size) for x in current_solution]
        neighbor_value = objective_function(neighbor_solution)

        # If the neighbor solution is better, update the current solution
        if neighbor_value < current_value:
            current_solution = neighbor_solution
            current_value = neighbor_value

    return current_solution, current_value

# Example usage
if __name__ == "__main__":
    # Set the initial solution, step size, and maximum iterations
    initial_solution = [random.uniform(-5, 5) for _ in range(3)]
    step_size = 0.1
    max_iterations = 1000

    # Run Hill Climbing algorithm
    final_solution, final_value = hill_climbing(initial_solution, step_size, max_iterations)

    # Output the result
    print("Initial Solution:", initial_solution)
    print("Final Solution:", final_solution)
    print("Final Objective Value:", final_value)
