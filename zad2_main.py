import graph_parser
import argparse



visitedList = []  
path_length = None
stars_count = None #przechowywujemy najwieksza liczbe gwiazdek
def depthFirst(graph, currentVertex, visited):
    global path_length
    global stars_count
    visited.append(currentVertex)
    for vertex in graph[currentVertex]:
        if vertex not in visited:
            depthFirst(graph, vertex, visited.copy())
    if visited[-1] in podnoza_list: #Sprawdzamy czy sciezka konczy sie na podnozu
        if path_length == None: # dla pierwszego wywolania
            visitedList.append(visited)
            path_length = len(visited)
            stars_count = sum([stars.get(vertex,vertex) for vertex in visited])
        else:
            if len(visited)< path_length: #sprawdzamy czy aktualna sciezka jest krotsza niz poprzednia
                visitedList.clear()
                visitedList.append(visited) #dodajemy element
                stars_count = sum([stars.get(vertex,vertex) for vertex in visited])
                path_length = len(visited)
            elif len(visited) == path_length:
                if stars_count < sum([stars.get(vertex,vertex) for vertex in visited]): #czyscimy tablice i dodajemy element z najwieksza liczba gwiazdek, i aktualizujemy stars_count
                    visitedList.clear()
                    visitedList.append(visited) #dodajemy element
                    stars_count = sum([stars.get(vertex,vertex) for vertex in visited])


if __name__ == "__main__":
    # Parsing script arguments (path to file with data)
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=argparse.FileType("r"))
    args = parser.parse_args()
    graph, podnoza_list, stars = graph_parser.get_graph(args.file.name)
    stars["szczyt"] = 0 #dodanie szczytu o wartosci gwiazdki 0 w celu poprawnego dzialania algorytmu
    
    depthFirst(graph, "szczyt" , [])

    print("Optymalna sciezka to: ")
    print(visitedList)
