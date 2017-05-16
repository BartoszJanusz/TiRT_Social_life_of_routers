#!/usr/bin/python3

from graph_tool.all import *
import time
import matplotlib

def load_graph_edges( file ):
    edges=[]
    with open(file) as f:
        for line in f:
            edges.append([int(x) for x in line.split()])
    return edges

def load_spanning_tree_nodes( file ):
    nodes=[]
    with open(file) as f:
        for line in f:
            nodes.append(int(line))
    return nodes

def load_graph( file ):
	g = Graph(directed=False)
	g.add_edge_list( load_graph_edges(file))
	return g

load_graph('./python_graph.dat')
