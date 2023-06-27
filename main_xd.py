import graph_parser
graph, podnuza_list, stars = graph_parser.get_graph("input.txt")

# graph = {
#     0: [1, 4, 6],
#     1: [2],
#     2: [3, 9],
#     3: [],
#     9: [],
#     4: [5],
#     5: [],
#     6: [8, 7],
#     8: [],
#     7: [],
# }

# stars = {
#     0: [0],  #preprocessing
#     1: [0],
#     2: [5],
#     3: [4],
#     4: [2],
#     5: [1],
#     6: [4],
#     7: [5],
#     8: [4],
#     9: [3],
# }

visitedList = []  

def indeksy_najwiekszych_elementow(list):
    biggest = max(list)
    indices = [i for i, x in enumerate(list) if x == biggest]
    return indices

def print_items_by_index(list, indices):
    for indeks in indices:
        print(list[indeks])

def depthFirst(graph, currentVertex, visited):
    visited.append(currentVertex)
    for vertex in graph[currentVertex]:
        if vertex not in visited:
            depthFirst(graph, vertex, visited.copy()) 
    visitedList.append(visited)

depthFirst(graph, "szczyt" , [])


list_sciez_podn = []

for list_i in visitedList:
    if list_i[-1] in podnuza_list:
        list_sciez_podn.append(list_i)



smallest_length = min(len(element) for element in list_sciez_podn)
smallest_lists = [element for element in list_sciez_podn if len(element) == smallest_length]

new_list = [[stars.get(vertex, vertex) for vertex in element] for element in smallest_lists]

new_list_v2 = [sum(sublist) for sublist in new_list]

#sum_list = [sum(sublist) for sublist in new_list_v2]

index_list = indeksy_najwiekszych_elementow(new_list_v2)


print(visitedList)
print(list_sciez_podn)
print(smallest_lists)
print(new_list)
print(new_list_v2)
#print(sum_list)
print(index_list)

print("optymalne sciezki to: ")
print_items_by_index(smallest_lists, index_list)