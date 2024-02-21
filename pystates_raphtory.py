"""
For Raphtory objects

"""
from raphtory import Graph
from pystates import all_spectrums, snapshot_dist
import numpy as np

# 1. Convert undirected edges into adjency matrices. Perhaps for each timestamp unit or perhaps give it a time window.
#   if time window - for how long? - Could do an hour snapshots
#
# 2. Put the adjency matrices into a dict, where the key is the index of the window and val is the adjency matrix
#
# what kind of data strucure should the dictionary key be? 
# I assume it would be numpy 2d array

#
#

# Identify all unique nodes
#print(list(g.vertices.name))
# [ms3123,ms323,...]

# Create a node index map
node_index = {node_name: i for i, node_name in enumerate(list(g.vertices.name))}
#print(node_index)
# [ms3123:0, ms323:1,...]

# Initialise adjacency matrix
adjacency_matrix = np.zeros((len(list(g.vertices.name)), len(list(g.vertices.name))), dtype=int)
#[[0 0 0 ... 0 0 0]
# [0 0 0 ... 0 0 0]
# [0 0 0 ... 0 0 0]
# ...
# [0 0 0 ... 0 0 0]
# [0 0 0 ... 0 0 0]
# [0 0 0 ... 0 0 0]]


# Populate adjacency matrix
for edge in g.edges:
    src_index = node_index[edge.src.name]
    dst_index = node_index[edge.dst.name]

    adjacency_matrix[src_index, dst_index] = 1

#print(adjacency_matrix)
#[[0 1 0 ... 0 0 0]
# [0 0 0 ... 0 0 0]
# [0 0 1 ... 0 0 0]
# ...
# [0 0 0 ... 0 0 0]
# [0 0 0 ... 0 0 0]
# [0 0 0 ... 0 0 0]]

A_dict = {'1': adjacency_matrix}
print(A_dict)

# Pickle the variables