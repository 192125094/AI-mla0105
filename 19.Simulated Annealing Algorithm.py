import numpy as np
import math
import random

# Define the objective function (you need to modify this based on your specific problem)
def objective_function(x):
    return x**2 - 4*x + 4

# Simulated Annealing function
def simulated_annealing(initial_state, temperature, cooling_rate, iterations):
    current_state = initial_state
    current_energy = objective_function(current_state)

    for _ in range(iterations):
        # Generate a random neighboring state
        neighbor_state = current_state + np.random.uniform(-0.5, 0.5)

        # Calculate the energy (objective function value) of the neighboring state
        neighbor_energy = objective_function(neighbor_state)

        # Calculate the energy difference between the current state and the neighboring state
        energy_difference = neighbor_energy - current_energy

        # Accept the neighboring state if it has lower energy or with a certain probability
        if energy_difference < 0 or random.random() < math.exp(-energy_difference / temperature):
            current_state = neighbor_state
            current_energy = neighbor_energy

        # Cool down the temperature
        temperature *= 1 - cooling_rate

    return current_state, current_energy

# Set initial parameters
initial_state = 0.0
initial_temperature = 100.0
cooling_rate = 0.01
iterations = 1000

# Run simulated annealing
final_state, final_energy = simulated_annealing(initial_state, initial_temperature, cooling_rate, iterations)

# Print the results
print("Simulated Annealing Result:")
print("Final State:", final_state)
print("Final Energy:", final_energy)
