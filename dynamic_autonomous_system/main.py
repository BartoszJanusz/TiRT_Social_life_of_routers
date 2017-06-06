import graph_tool.all as gt
import graph_tool.centrality as gtc
import matplotlib.pyplot as plt

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


def load_alg_data(file):
    alg = open(file, 'r')
    tab = []
    for line in alg:
        tmp = []
        for element in line.split(' '):
            if element != '\n':
                tmp.append(float(element))
        tab.append(tmp)
    return tab


file_list = [line.rstrip('\n') for line in open('../data/graphs_no_outliers.txt')]

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
    x.append(i)

funcs = [verticies_by_days, edges_by_days, density_by_days, avg_vertex_degree_by_day]
ylabels = ["Number vertices", "Number edges", "Density", "Avg vertex degree"]

# for i, f in enumerate(funcs):
#     x, y = f(graphs)
#     plt.figure(i)
#     plt.xlabel("Graph number")
#     plt.ylabel(ylabels[i])
#    plt.plot(y, 'bo', ms=2.0)
#    plt.show(block=False)

# closeness_file = open('/home/bartosz/TiRT_Social_life_of_routers/data/alg_results/closeness_avg.txt', 'w')

funcs = [np.mean, np.median, np.max, np.min]
prop = ['ro', 'bo', 'go', 'mo']

algorithm_array = load_alg_data("../data/alg_results/closeness_avg.txt")
print("algorithm_array: ", len(algorithm_array))
plt.figure()
plt.xlabel("Graph number")
plt.ylabel("Mean closeness")
for i, f in enumerate(funcs):
    x1, y1 = function_value_for_2dim_array_by_day(algorithm_array, f)
    plt.plot(y1, prop[i], ms=2.0)



plt.show(block=False)

# x2, y2 = function_value_for_2dim_array_by_day( algorithm_array, np.median )
# x3, y3 = function_value_for_2dim_array_by_day( algorithm_array, np.min )
# x4, y4 = function_value_for_2dim_array_by_day( algorithm_array, np.max )

page_rank_file = open('/home/bartosz/TiRT_Social_life_of_routers/data/alg_results/pagerank.txt', 'w')

funcs = [gtc.pagerank]
for f in funcs:
    x, y = avg_function_value_by_day(graphs, f)
    for yi in y:
        for yii in yi:
            page_rank_file.write("%f " % yii)
        page_rank_file.write('\n')
    page_rank_file.close()

funcs = [np.mean, np.median, np.min]
prop = ['ro', 'bo', 'go', 'mo']

algorithm_array = load_alg_data("../data/alg_results/pagerank.txt")
print("algorithm_array: ", len(algorithm_array))
plt.figure()
plt.xlabel("Graph number")
plt.ylabel("Mean closeness")
for i, f in enumerate(funcs):
    x1, y1 = function_value_for_2dim_array_by_day(algorithm_array, f)
    plt.plot(y1, prop[i], ms=2.0)

plt.show()
# plt.figure(4)
# plt.xlabel("Graph number")
# plt.ylabel("Closeness avg")
# plt.plot(y, 'bo', ms=2.0)
# plt.show(block=False)
#
# plt.show()

# print( zip( x, y) )
# print( x , y)

# alg = gt.pagerank(g)
# gt.graph_draw(g, vertex_fill_color=alg, vertex_size=gt.prop_to_size(alg, mi=5, ma=100),
#               vorder=alg, vcmap=matplotlib.cm.gnuplot, output_size=(10000, 10000),
#               output="../graph_png/pagerank_8k.png")
