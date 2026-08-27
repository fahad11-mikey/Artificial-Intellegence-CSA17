import sys
from itertools import permutations

# Define the Distance Matrix (Adjacency Matrix)
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Total number of cities
num_cities = len(distance_matrix)

# Start city index
start_city = 0

def calculate_path_cost(path, matrix):
    """Calculates the total travel cost for a given path sequence."""
    total_cost = 0
    current_city = start_city
    
    # Calculate costs between sequential cities in the path
    for next_city in path:
        total_cost += matrix[current_city][next_city]
        current_city = next_city
        
    # Complete the loop by returning back to the start city
    total_cost += matrix[current_city][start_city]
    return total_cost

def solve_tsp(matrix, start):
    """Explores the state-space using brute-force search to find the optimal path."""
    # Generate list of all cities excluding the start city
    cities_to_visit = [city for city in range(num_cities) if city != start]
    
    # Initialize trackers for the minimum route
    min_cost = sys.maxsize
    optimal_path = []
    
    print("Exploring State-Space (Possible Routes & Costs):")
    print("-" * 50)
    
    # Generate every single possible permutation of the path
    all_possible_routes = permutations(cities_to_visit)
    
    for route in all_possible_routes:
        # Calculate cost for the current path permutation
        current_cost = calculate_path_cost(route, matrix)
        
        # Format the full round-trip route string for logging
        full_route_sequence = [start] + list(route) + [start]
        route_string = " -> ".join(f"City {c}" for c in full_route_sequence)
        print(f"Route: {route_string} | Total Cost: {current_cost}")
        
        # If a cheaper route is found, update trackers
        if current_cost < min_cost:
            min_cost = current_cost
            optimal_path = full_route_sequence
            
    print("-" * 50)
    return optimal_path, min_cost

# Run the program
if __name__ == "__main__":
    print(f"Starting Travelling Salesman Problem from City {start_city}...\n")
    
    best_route, lowest_cost = solve_tsp(distance_matrix, start_city)
    
    # Output the final optimal solution
    print("\nOptimal Solution Found!")
    optimal_route_string = " -> ".join(f"City {c}" for c in best_route)
    print(f"Best Route: {optimal_route_string}")
    print(f"Minimum Travel Cost: {lowest_cost}")
