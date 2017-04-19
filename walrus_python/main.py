from graph_tool import centrality
from graph_tool.all import *
import time
from walrus_graph import walrus_output


# Wczytać graf inną funkcją!!

def load_graph(file):
    gf = open(file, mode='r')
    vertices = []

    for line in gf:
        v = line.split(',')
        vertices.append(int(v[0]))

    vertices = set(vertices)
    vertices = list(vertices)
    vertices.sort()
    v_dict = {}

    for i, v in enumerate(vertices):
        v_dict[v] = i

    g = Graph()
    g.add_vertex(len(vertices))

    gf.seek(0, 0)

    edges = []
    for line in gf:
        sl = line.split(',')
        v1 = v_dict[int(sl[0])]
        v2 = v_dict[int(sl[1])]
        edges.append((v1, v2))
        g.add_edge(v1, v2)

    gf.close()

    st = min_spanning_tree(g, weights=None, root=0)

    for e in st.get_array():
        print(e)

    g.set_edge_filter(st, inverted=False)
    stg = Graph(g, prune=True)
    g.clear_filters()
    g.set_edge_filter(st, inverted=True)
    non_stg = Graph(g, prune=True)
    print("St edges: " + str(stg.num_edges()) + " : Non_st edges: " + str(non_stg.num_edges()))
    g.clear_filters()

    non_stg_edges = []
    for e in non_stg.get_edges():
        non_stg_edges.append(frozenset({e[0], e[1]}))

    print(len(non_stg_edges))

    non_stg_edges = set(non_stg_edges)

    print(len(non_stg_edges))

    for e in non_stg_edges:
        l = list(e)
        stg.add_edge(l[0], l[1])

    return stg, st.get_array()


# g = Graph(load_graph_from_csv("graph_as.csv", directed=False, ecols=(0, 1), csv_options={'delimiter': ','}))
g, st = load_graph("graph_as_nolabel.csv")

start = time.time()
#pos = sfdp_layout(g)
#graph_draw(u, pos, output_size=(10000, 10000), output="st_as_10k.png")
end = time.time()

# edges = sorted(g.get_edges(), key=lambda x: x[0])

walrus_output(g, st)

print("Generate png: ", end - start)
