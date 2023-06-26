graph = {
    0: [1, 4, 6],
    1: [2],
    2: [3, 9],
    3: [],
    9: [],
    4: [5],
    5: [],
    6: [8, 7],
    8: [],
    7: [],
}

stars = {
    0: [0],  #preprocessing
    1: [0],
    2: [5],
    3: [4],
    4: [2],
    5: [1],
    6: [4],
    7: [5],
    8: [4],
    9: [3],
}

visitedList = []  # Usunięcie [[]] - niepotrzebnej pustej listy

def indeksy_najwiekszych_elementow(lista):
    najwieksze = max(lista)
    indeksy = [i for i, x in enumerate(lista) if x == najwieksze]
    return indeksy

def drukuj_elementy_po_indeksach(lista, indeksy):
    for indeks in indeksy:
        print(lista[indeks])

def depthFirst(graph, currentVertex, visited):
    visited.append(currentVertex)
    for vertex in graph[currentVertex]:
        if vertex not in visited:
            depthFirst(graph, vertex, visited.copy())  # Używanie visited.copy()
    visitedList.append(visited)

depthFirst(graph, 0, [])

podnuza_list = [7, 5, 3, 9]

lista_sciez_podn = []

for list_i in visitedList:
    if list_i[-1] in podnuza_list:
        lista_sciez_podn.append(list_i)



najmniejsza_dlugosc = min(len(element) for element in lista_sciez_podn)
najmniejsze_listy = [element for element in lista_sciez_podn if len(element) == najmniejsza_dlugosc]

nowa_lista = [[stars.get(vertex, vertex) for vertex in element] for element in najmniejsze_listy]

nowa_lista_v2 = [sum(sublist, []) for sublist in nowa_lista]

sum_list = [sum(sublist) for sublist in nowa_lista_v2]

index_list = indeksy_najwiekszych_elementow(sum_list)


print(visitedList)
print(lista_sciez_podn)
print(najmniejsze_listy)
print(nowa_lista)
print(nowa_lista_v2)
print(sum_list)
print(index_list)

print("optymalne sciezki to: ")
drukuj_elementy_po_indeksach(najmniejsze_listy, index_list)