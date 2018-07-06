import sys, itertools
from collections import defaultdict

def journeyToMoon(n, astronaut):
    # Complete this function
    # trans astronaut pair list to graph, assume each astronaut in their own country initially
    connected_graphs = [] # [[graph1], [graph2], ...]
    dict_ast_country = defaultdict(list) # {key_astronaut:val_country, }
    for i in range(0, n):
        new_country = [i]
        connected_graphs.append(new_country)
        dict_ast_country[i] = new_country
    # re-categorize astronauts to actual country and integrate countries according to given info.
    for pair in astronaut:
        if dict_ast_country[pair[0]] is not dict_ast_country[pair[1]]:
            dict_ast_country[pair[0]] += dict_ast_country[pair[1]]
            to_be_deleted_country = dict_ast_country[pair[1]]
            for ast in to_be_deleted_country:
                dict_ast_country[ast] = dict_ast_country[pair[0]]
            connected_graphs.remove(to_be_deleted_country)
    # depart graph as independent subgraph, each subgraph is a country
    # caculate pair of countries, eg c1, c2, all possibility pairs = N(c1) x N(c2)
    country_pairs = list(itertools.combinations(connected_graphs, 2))
    all_counts = 0
    for cpair in country_pairs:
        all_counts += len(cpair[0]) * len(cpair[1])
    # accumulate all pair counts
    return all_counts

if __name__ == "__main__":
    n, p = input().strip().split(' ')
    n, p = [int(n), int(p)]
    astronaut = []
    for astronaut_i in range(p):
        astronaut_t = [int(astronaut_temp) for astronaut_temp in input().strip().split(' ')]
        astronaut.append(astronaut_t)
    result = journeyToMoon(n, astronaut)
    print(result)