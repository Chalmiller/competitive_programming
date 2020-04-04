num_cities = int(input())
city_graph = []

for test_cases in range(num_cities - 1):
    city = input().split(" ")
    city_graph.append(city)
blocked = [int(block) for block in input().split(" ")]
print(sum(blocked))


