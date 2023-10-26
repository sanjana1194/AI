import itertools

def total_distance(path, distances):
    distance = 0
    for i in range(len(path) - 1):
        distance += distances[path[i]][path[i+1]]
    distance += distances[path[-1]][path[0]]
    return distance

if _name_ == "_main_":
    n = int(input("Enter the number of cities: "))
   
    cities = []
    distances = {}

    for i in range(n):
        city = input(f"Enter name of city {i+1}: ")
        cities.append(city)
        distances[city] = {}

    for i in range(n):
        for j in range(i+1, n):
            d = float(input(f"Enter distance between {cities[i]} and {cities[j]}: "))
            distances[cities[i]][cities[j]] = d
            distances[cities[j]][cities[i]] = d

    shortest_distance = float('inf')
    shortest_path = None

    for path in itertools.permutations(cities):
        current_distance = total_distance(path, distances)
        if current_distance < shortest_distance:
            shortest_distance = current_distance
            shortest_path = path

    print(f"Shortest path is {' -> '.join(shortest_path)} with total distance: {shortest_distance}")
