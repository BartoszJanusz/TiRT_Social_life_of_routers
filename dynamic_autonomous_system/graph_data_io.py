from graph_stats import *

def load_data(file_name):
    file = open(file_name, 'r')
    tab = []
    for line in file:
        tab.append([ float(element) for element in line.split() ])
    return tab

def save_data( file_name, graphs, function, return_id = 0):
    file = open(file_name, 'w')
    x, data_set = apply_function_to_graphs(graphs, function, return_id )
    for value_list in data_set:
        for value in value_list:
            file.write("%f " % value)
        file.write('\n')
    file.close()
