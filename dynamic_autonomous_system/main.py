from os import listdir
import graph_tool.all as gt
import graph_tool.centrality as gtc
import time

import matplotlib.pyplot as plt
import numpy as np

#import statsmodels.api as smapi
#from statsmodels.formula.api import ols

from graph_stats import *


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

def reject_outliers(data, m=3):
    return [x for x in data if abs(x - np.mean(data)) < m * np.std(data) ]

file_list = listdir("../data/gt_graphs")
file_list.sort()

print(file_list)

graphs = []
x = []
y = []
page_rank_max = []

for i, file in enumerate(file_list):
    g = gt.Graph()
    g.load("../data/gt_graphs/" + file, fmt='gt')
    graphs.append(g)
    print("Loaded ", i, " graph")
    y.append(g.num_vertices())

matlab_file = open("matlab_data.txt", mode='w')
for i in y:
    matlab_file.write(str(i) + "\n")
matlab_file.close()
