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
	for e in load_graph_edges(file):
		g.add_edge(e[0], e[1])
	return g

# load_graph('./python_graph.dat')
