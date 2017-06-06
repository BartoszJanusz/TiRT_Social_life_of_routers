from graph_data_io import *
from graph_stats import *
from custom_plot import *


def pause():
    programPause = input("Press the <ENTER> key to continue...")

def plot_basic_functions(graphs):

    func = [get_series_of_vertices,
            get_series_of_edges,
            get_series_of_density,
            get_series_of_avg_vertex_degree]
    data = []

    for f in func:
        x, y = f(graphs)
        plot([(f.__name__.replace('get_series_of_', ''), y)], ['bo'], ["Title", 'X', 'Y'], 'linear')

def plot_gt_algo(array, title):
    func = [np.mean, np.median, np.max, np.min]
    data = []
    for f in func:
        x, y = apply_np_function_to_values(array, f)
        data.append((f.__name__, y))

    plot(data, ['bo', 'ro', 'go', 'mo'], [title, 'X', 'Y'], 'log')


graphs = load_graphs()

plot_basic_functions(graphs)

betw = load_data('../data/alg_results/betweenness_vertices.txt')
clos = load_data('../data/alg_results/closeness.txt')
pg = load_data('../data/alg_results/pagerank.txt')

plot_gt_algo(betw, 'Betweenness')
plot_gt_algo(clos, 'Closeness')
plot_gt_algo(pg, 'Pagerank')
pause()