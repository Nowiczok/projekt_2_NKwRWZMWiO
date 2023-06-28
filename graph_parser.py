
def remove_whitespaces(lines):
    new_lines = []
    for line in lines:
        new_line = line.replace(" ", "")
        new_line = new_line.replace("\n", "")
        new_lines.append(new_line)
    return new_lines


def remove_comments(lines):
    new_lines = []
    for line in lines:
        if line[0:2] != "//":
            new_lines.append(line)
    return new_lines


def remove_empty_lines(lines):
    new_lines = []
    for line in lines:
        if line != "":
            new_lines.append(line)
    return new_lines


def extract_neighborhood_list(lines):
    neighborhood_list = []
    line_nbr = 1
    while lines[line_nbr] != "}":
        neighborhood_list.append(lines[line_nbr])
        line_nbr += 1
    return neighborhood_list, line_nbr


def convert_lines_to_graph(neighborhood_list_lines):
    graph = {}
    podnoze_list = []
    for line in neighborhood_list_lines:
        [key, values_together_podnoze] = line.split(":")
        [values_together, podnoze] = values_together_podnoze.split(";")
        values = values_together.split(",")
        if values == [""]:
            graph[key] = []
        else:
            graph[key] = values
        if podnoze != "":
            podnoze_list.append(key)
    return graph, podnoze_list


def extract_stars_list(lines, start_line):
    stars_list = []
    line_nbr = start_line+2
    while lines[line_nbr] != "}":
        stars_list.append(lines[line_nbr])
        line_nbr += 1
    return stars_list, line_nbr


def conver_lines_to_stars_list(star_list_lines):
    stars_list = {}
    for line in star_list_lines:
        [key, stars] = line.split(":")
        stars_list[key] = int(stars)
    return stars_list


def get_graph(path):
    f = open(path, "r")
    lines = f.readlines()
    lines = remove_whitespaces(lines)
    lines = remove_comments(lines)
    lines = remove_empty_lines(lines)

    neighborhood_list_lines, end_line_nbr = extract_neighborhood_list(lines)
    graph, podnoze_list = convert_lines_to_graph(neighborhood_list_lines)

    stars_list_lines, end_line_nbr = extract_stars_list(lines, end_line_nbr)
    stars_list = conver_lines_to_stars_list(stars_list_lines)
    return graph, podnoze_list, stars_list
