from functools import partial

import numpy as np

from custom_plot import *
from graph_data_io import *
from graph_stats import *


def plot_basic_functions(graphs):
    func = [get_series_of_vertices,
            get_series_of_edges,
            get_series_of_density]
    titles = ['Number vertices', 'Number edges', 'Graph density']

    for i, f in enumerate(func):
        y = f(graphs)
        plot([(f.__name__.replace('get_series_of_', ''), y)], ['bo'], [titles[i], 'Graph ID', 'Value'], 'linear')


def plot_gt_algo(array, title):
    func = [np.min]
    data = []
    for f in func:
        y = apply_np_function_to_values(array, f)
        data.append((f.__name__, y))

    plot(data, ['bo', 'ro', 'go', 'mo'], [title, 'Graph ID', 'Algorithm value'], 'linear')


graphs = load_graphs()

plot_basic_functions(graphs)

betw = load_data('../data/alg_results/betweenness_vertices.txt')
clos = load_data('../data/alg_results/closeness.txt')
pg = load_data('../data/alg_results/pagerank.txt')
degree = get_series_of_vertex_degrees(graphs)
degree_percentile = [('Percentile 99.99', apply_np_function_to_values(degree, lambda e: np.percentile(e, 99.99))),
                     ('Percentile 99.9', apply_np_function_to_values(degree, lambda e: np.percentile(e, 99.9))),
                     ('Percentile 99.5', apply_np_function_to_values(degree, lambda e: np.percentile(e, 99.5))),
                     ('Percentile 99.0', apply_np_function_to_values(degree, lambda e: np.percentile(e, 99.0))),
                     ('Percentile 95.0', apply_np_function_to_values(degree, lambda e: np.percentile(e, 95.0)))]

plot_gt_algo(betw, 'Betweenness')
plot_gt_algo(clos, 'Closeness')
plot_gt_algo(pg, 'Pagerank')
plot_gt_algo(degree, 'Nodes\' degrees')
plot(degree_percentile, ['bo', 'ro', 'go', 'mo', 'ko'], ['Degree percentile', 'Graph ID', 'Percentile'], 'linear')
plt.show()
