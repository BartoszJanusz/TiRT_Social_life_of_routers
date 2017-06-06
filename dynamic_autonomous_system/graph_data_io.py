from graph_stats import *
import graph_tool.all as gt


def load_data(file_name):
    file = open(file_name, 'r')
    tab = []
    for line in file:
        tab.append([float(element) for element in line.split()])
    return tab


def save_data(file_name, data_sets):
    file = open(file_name, 'w')
    for value_list in data_sets:
        for value in value_list:
            file.write("%f " % value)
        file.write('\n')
    file.close()


def load_graphs():
    file_list = [line.rstrip('\n') for line in open('../data/graphs_no_outliers.txt')]
    graphs = []
    for i, file in enumerate(file_list):
        g = gt.Graph()
        g.load("../data/gt_graphs/" + file, fmt='gt')
        graphs.append(g)
    return graphs


def load_graph(file):
    gf = open(file, mode='r')

    # Wczytaj wierzchołki do tablicy (listy).
    vertices = []
    for line in gf:
        v = line.split('\t')
        vertices.append(int(v[0]))
        vertices.append(int(v[1]))

    # Usuń wierzchołki występujące wielokrotnie.
    vertices = set(vertices)
    vertices = list(vertices)
    vertices.sort()
    # print('{:35}'.format("Number vertices"), len(vertices))

    # Wierzcholki w tablicy nie są ciągiem liczb naturalnych, tylko ciągiem numerów ID. Robimy słownik który powiąże ID z numerem wierzchołka.
    v_dict = {}
    for i, v in enumerate(vertices):
        v_dict[v] = i

    g = gt.Graph(directed=False)
    g.add_vertex(len(vertices))

    # Wróć na początek pliku.
    gf.seek(0, 0)

    # Wczytaj krawedzie do listy.
    edges = set()
    for line in gf:
        sl = line.split('\t')
        v1_id = int(sl[0])
        v2_id = int(sl[1])
        if v1_id != v2_id:
            v1 = v_dict[int(sl[0])]
            v2 = v_dict[int(sl[1])]
            edges.add(frozenset([v1, v2]))
    gf.close()

    #    edges = set(edges)

    for e in edges:
        e = list(e)
        g.add_edge(e[0], e[1])

    return g
