import os 
from data import read_dataset
from master_problem import solve_stochastic_cflp

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Set DATA_DIR to the correct location
DATA_DIR = os.path.join(script_dir, "../data/")

print("DATA_DIR:", DATA_DIR)  # Debugging output

if __name__ == "__main__":
    # file path to the dataset
    datafile = DATA_DIR + "p51"

    # Read the dataset from the file
    data = read_dataset(datafile)

    # Solve the Capacitated Facility Location Problem (CFLP) model and obtain the optimal solution
    solution = solve_stochastic_cflp(data)

    # Print solution information
    print("Objective value:    ", solution.objective_value)
    print("Open facilities:    ", [j for j in data.J if solution.locations[j] > 0.5])
    print("Solution time (sec):", solution.solution_time)
    print("No. of BD cuts generated:", sum(solution.num_cuts_mip[s] for s in data.S))
    print("No. of BD cuts generated (at node relaxation):", sum(solution.num_cuts_rel[s] for s in data.S))
    print("No. of explored Branch-and-Bound nodes:", solution.num_bnb_nodes)

    