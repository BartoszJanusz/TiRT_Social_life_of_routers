import graph_tool.stats as stats
import graph_tool.centrality as cents
import numpy as np


def verticies_by_days(graphs):
    x = []
    y = []
    for i, g in enumerate(graphs):
        y.append(g.num_vertices())
        x.append(i)
    return x, y


def edges_by_days(graphs):
    x = []
    y = []
    for i, g in enumerate(graphs):
        y.append(g.num_edges())
        x.append(i)
    return x, y


def density_by_days(graphs):
    x = []
    y = []
    for i, g in enumerate(graphs):
        y.append(2 * g.num_edges() / (g.num_vertices() * (g.num_vertices() - 1)))
        x.append(i)
    return x, y


def avg_vertex_degree_by_day(graphs):
    x = []
    y = []
    for i, g in enumerate(graphs):
        y.append(stats.vertex_average(g, 'total'))
        x.append(i)
    return x, y


def avg_function_value_by_day(graphs, function):
    x = []
    y = []
    for i, g in enumerate(graphs):
        values = function(g)
        y.append(values.get_array())
        x.append(i)
        print("func for ", i)
    return x, y
