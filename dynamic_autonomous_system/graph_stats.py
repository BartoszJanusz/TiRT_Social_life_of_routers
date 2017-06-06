import graph_tool.stats as stats
import graph_tool.centrality as cents
import numpy as np


def get_series_of_vertices(graphs):
    x = []
    y = []
    for i, g in enumerate(graphs):
        y.append(g.num_vertices())
        x.append(i)
    return x, y


def get_series_of_edges(graphs):
    x = []
    y = []
    for i, g in enumerate(graphs):
        y.append(g.num_edges())
        x.append(i)
    return x, y


def get_series_of_density(graphs):
    x = []
    y = []
    for i, g in enumerate(graphs):
        y.append(2 * g.num_edges() / (g.num_vertices() * (g.num_vertices() - 1)))
        x.append(i)
    return x, y


def get_series_of_avg_vertex_degree(graphs):
    x = []
    y = []
    for i, g in enumerate(graphs):
        y.append(stats.vertex_average(g, 'total'))
        x.append(i)
    return x, y


def apply_function_to_graphs(graphs, function, return_id = 0):
    x = []
    y = []
    for i, g in enumerate(graphs):
        values = function(g)
        if type(values) is tuple:
            y.append(values[return_id].get_array())
        else:
            y.append(values.get_array())
        x.append(i)
    return x, y

def apply_function_to_values( algorithm_array, function ):
    x = []
    y = []
    for i, element in enumerate(algorithm_array):
        value = function(element)
        y.append( value )
        x.append(i)
    return x, y
