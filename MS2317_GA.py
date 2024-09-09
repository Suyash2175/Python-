import numpy as np
import matplotlib.pyplot as plt
import random
import math

# Function to read city names and generate random coordinates
def read_cities(file_name):
    cities = []
    with open(file_name, 'r') as f:
        for line in f:
            city = line.strip()
            if city:
                # Generate random coordinates for cities
                x = random.uniform(60.0, 100.0)  # Random longitude for Indian cities
                y = random.uniform(8.0, 35.0)    # Random latitude for Indian cities
                cities.append((city, x, y))
            else:
                print(f"Skipping invalid line: {line}")
    return cities

# Function to calculate distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[1] - city2[1])**2 + (city1[2] - city2[2])**2)

# Function to calculate total distance of a route
def total_distance(route, cities):
    total_dist = 0
    for i in range(len(route) - 1):
        total_dist += distance(cities[route[i]], cities[route[i+1]])
    total_dist += distance(cities[route[-1]], cities[route[0]])  # Add distance from last city to first city
    return total_dist

# Genetic Algorithm
def genetic_algorithm(cities, population_size, generations, mutation_rate):
    # Initialize population
    population = [random.sample(range(len(cities)), len(cities)) for _ in range(population_size)]

    avg_fitness = []
    best_distances = []  # To track the best distance in each generation
    for generation in range(generations):
        # Calculate fitness (1 / total distance) for each route
        fitness = [1 / total_distance(route, cities) for route in population]
        total_distances = [total_distance(route, cities) for route in population]

        # Select parents using tournament selection
        parents = []
        for _ in range(population_size):
            tournament = [random.randint(0, population_size-1) for _ in range(3)]
            winner = np.argmax([fitness[i] for i in tournament])
            parents.append(population[tournament[winner]])

        # Crossover (order crossover)
        offspring = []
        for _ in range(population_size):
            parent1, parent2 = random.sample(parents, 2)
            child = parent1[:len(parent1)//2] + [city for city in parent2 if city not in parent1[:len(parent1)//2]]
            offspring.append(child)

        # Mutation (swap two cities)
        for i in range(population_size):
            if random.random() < mutation_rate:
                idx1, idx2 = random.sample(range(len(offspring[i])), 2)
                offspring[i][idx1], offspring[i][idx2] = offspring[i][idx2], offspring[i][idx1]

        # Replace population with offspring
        population = offspring

        # Track the best route and its distance
        best_route_idx = np.argmax(fitness)
        best_route = population[best_route_idx]
        best_distance = total_distances[best_route_idx]
        best_distances.append(best_distance)

        # Plot path tracing with city names at intermediate stages
        plt.clf()
        plt.scatter([cities[i][1] for i in range(len(cities))], [cities[i][2] for i in range(len(cities))])
        for i in range(len(best_route) - 1):
            plt.plot([cities[best_route[i]][1], cities[best_route[i+1]][1]], [cities[best_route[i]][2], cities[best_route[i+1]][2]], 'b-')
        plt.plot([cities[best_route[-1]][1], cities[best_route[0]][1]], [cities[best_route[-1]][2], cities[best_route[0]][2]], 'b-')
        for i in range(len(cities)):
            plt.annotate(cities[i][0], (cities[i][1], cities[i][2]))
        plt.title(f'Generation {generation+1}')
        plt.pause(0.01)

        # Calculate average fitness and track it
        avg_fitness.append(np.mean(fitness))

    # Plot increase in average fitness from generation to generation
    plt.clf()
    plt.plot(avg_fitness)
    plt.xlabel('Generation')
    plt.ylabel('Average Fitness (1 / Distance)')
    plt.title('Increase in Average Fitness')
    plt.show()

    # Plot decrease in best route distance over generations
    plt.clf()
    plt.plot(best_distances)
    plt.xlabel('Generation')
    plt.ylabel('Best Distance')
    plt.title('Decrease in Best Route Distance')
    plt.show()

    # Print final output of the best route and distance
    best_final_route = population[np.argmax(fitness)]
    best_final_distance = min(best_distances)
    print("Final Best Route:")
    for i in best_final_route:
        print(cities[i][0], end=" -> ")
    print(cities[best_final_route[0]][0])  # To complete the loop
    print(f"Final Best Distance: {best_final_distance:.2f}")

# Main function
def main():
    cities = read_cities('india_cities.txt')  # Make sure this file only contains city names, one per line
    if not cities:
        print("No valid cities loaded.")
        return

    population_size = 100
    generations = 100
    mutation_rate = 0.01
    genetic_algorithm(cities, population_size, generations, mutation_rate)

if __name__ == '__main__':
    main()
