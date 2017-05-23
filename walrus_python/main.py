from graph_tool import centrality
from graph_tool.all import *
import time
import matplotlib
from walrus_graph import walrus_output
from graph_load import load_graph, load_spanning_tree_nodes, load_graph_edges


# def load_graph(file):
#     gf = open(file, mode='r')
#
#     # Wczytaj wierzchołki do tablicy (listy).
#     vertices = []
#     for line in gf:
#         v = line.split(',')
#         vertices.append(int(v[0]))
#
#     # Usuń wierzchołki występujące wielokrotnie.
#     vertices = set(vertices)
#     vertices = list(vertices)
#     vertices.sort()
#     print('{:35}'.format("Number vertices"), len(vertices))
#
#     # Wierzcholki w tablicy nie są ciągiem liczb naturalnych, tylko ciągiem numerów ID. Robimy słownik który powiąże ID z numerem wierzchołka.
#     v_dict = {}
#     for i, v in enumerate(vertices):
#         v_dict[v] = i
#
#
#     g = Graph(directed=False)
#     g.add_vertex(len(vertices))
#
#     # Wróć na początek pliku.
#     gf.seek(0, 0)
#
#     # Wczytaj krawedzie do listy i grafu.
#     edges = []
#     for line in gf:
#         sl = line.split(',')
#         v1 = v_dict[int(sl[0])]
#         v2 = v_dict[int(sl[1])]
#         edges.append((v1, v2))
#         g.add_edge(v1, v2)
#         if v1 == 0 or v2 == 0:
#             print(v1, v2)
#     gf.close()
#
#     print('{:35}'.format("Number edges"), g.num_edges())
#     print("First vertex:", g.vertex(0, use_index=True))
#     # Zbuduj minimalne drzewo rozpinające.
#     st = min_spanning_tree(g, weights=None, root=g.vertex(0, use_index=False))
#     print(g.get_edges()[0])
#     # Zbuduj nowy graf zawierający wyłącznie drzewo rozpinające.
#     g.set_edge_filter(st, inverted=False)
#     stg = Graph(g, prune=True)
#     for e in stg.get_edges():
#         if e[1] == 0:
#             print(e)
#     #print(stg.edge(0, 64))
#
#     g.clear_filters()
#
#     #graph_draw(g, output_size=(3000, 3000), output="double_test_st.png")
#     g.set_edge_filter(st, inverted=True)
#     non_stg = Graph(g, prune=True)
#     print('{:35}'.format("St edges"), stg.num_edges())
#     print('{:35}'.format("Non_st edges"), non_stg.num_edges())
#     g.clear_filters()
#     # Władować krawędzie, które nie zawierają się w drzewie spinającym do tablicy i wywalić zdublowane.
#     non_stg_edges = []
#     for e in non_stg.get_edges():
#         non_stg_edges.append(frozenset({e[0], e[1]}))
#
#     print('{:35}'.format("Number non-st edges (list)"), len(non_stg_edges))
#
#     non_stg_edges = set(non_stg_edges)
#
#     print('{:35}'.format("Number non-st edges (set)"), len(non_stg_edges))
#     cnt = 0
#     #Dodać pozostałe (jeszcze nie obecne w drzewie) krawędzie do drzewa.
#     for e in non_stg_edges:
#         l = list(e)
#         if not(stg.edge(l[0], l[1])):
#             stg.add_edge(l[0], l[1])
#             cnt += 1;
#     print('{:35}'.format("Number edges added to st"), cnt)
#     print('{:35}'.format("Number graph edges"), stg.num_edges())
#
#     stg_fixed = Graph(directed=False)
#     stg_fixed.add_vertex(stg.num_vertices())
#
#     for e in stg.edges():
#         #print("Source:", e.source())
#         s = e.source()
#         t = e.target()
#
#         if s > t:
#             print("s=", s, "t=", t)
#             stg_fixed.add_edge(t, s, add_missing=False)
#         else:
#             stg_fixed.add_edge(s, t, add_missing=False)
#
#     print("First g edge:", stg_fixed.get_edges()[0])
#
#     for e in stg_fixed.edges():
#         print(e)
#     stg_fixed.set_directed(True)
#     return stg_fixed, min_spanning_tree(stg_fixed, weights=None, root=0).get_array()

# g = Graph(load_graph_from_csv("data/graph_as.csv", directed=False, ecols=(0, 1), csv_options={'delimiter': ','}))

def map_array(array):
    output = []
    max_val = max(array)
    min_val = min(array)
    ref_val = max_val - min_val

    for e in array:
        e = (e - min_val) / ref_val
        output.append(e)
    return output

def node_color(array):
    colors = []

    for e in array:
        colors.append(matplotlib.cm.gnuplot(e))
    return colors

def edge_color(array, edges):
    colors = []

    for e in edges:
        x = max(array[e[0]], array[e[1]])
        colors.append(matplotlib.cm.gnuplot(x))
    return colors

start = time.time()
g = load_graph("./python_graph.dat")
end = time.time()
print("--------------Time measurments--------------")
print('{:35}'.format("Load graph"), end - start)

start = time.time()
alg = pagerank(g)
end = time.time()
print('{:35}'.format("Algorithm"), end - start)

start = time.time()
# pos = sfdp_layout(g, vweight=alg)
end = time.time()
print('{:35}'.format("Layout calculation"), end - start)

start = time.time()
# graph_draw(g, vertex_fill_color=alg, vertex_size=prop_to_size(alg, mi=5, ma=100),
#           vorder=alg, vcmap=matplotlib.cm.gnuplot, output_size=(10000, 10000), output="g.png")
end = time.time()
print('{:35}'.format("Generate png"), end - start)

st = load_spanning_tree_nodes('python_spanning_tree.dat')

edges = load_graph_edges('python_graph.dat')
alg = map_array(alg)
walrus_output(g, edges, st, node_color(alg), edge_color(alg, edges))
