import graph_tool.stats as stats


def get_series_of_vertices(graphs):
    y = []
    for i, g in enumerate(graphs):
        y.append(g.num_vertices())

    return y


def get_series_of_edges(graphs):
    y = []
    for i, g in enumerate(graphs):
        y.append(g.num_edges())

    return y


def get_series_of_density(graphs):
    y = []
    for i, g in enumerate(graphs):
        y.append(2 * g.num_edges() / (g.num_vertices() * (g.num_vertices() - 1)))

    return y


def get_series_of_avg_vertex_degree(graphs):
    y = []
    for i, g in enumerate(graphs):
        y.append(stats.vertex_average(g, 'total'))

    return y


def get_series_of_vertex_degrees(graphs):
    y = []
    for g in graphs:
        y.append(g.degree_property_map('total').get_array())
    return y


def apply_gt_function_to_graphs(graphs, function, return_id=0):
    y = []
    for i, g in enumerate(graphs):
        values = function(g)
        if type(values) is tuple:
            y.append(values[return_id].get_array())
        else:
            y.append(values.get_array())

        print(i)
    return y


def apply_np_function_to_values(algorithm_array, function):
    y = []
    for i, element in enumerate(algorithm_array):
        value = function(element)
        y.append(value)

    return y
