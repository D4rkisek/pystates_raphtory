import os
from raphtory import Graph

# Specify the file path
binecode_path = "C:/ms_bincode/Graph_1"

# Load the file
if os.path.isfile(binecode_path):
    g = Graph.load_from_file(binecode_path)
    print(g)
else:
    print(f"File does not exist: {binecode_path}")



