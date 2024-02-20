"""
For Raphtory objects

"""

import Raphtory
from pystates import all_spectrums, snapshot_dist


# 1. Convert undirected edges into adjency matrices. Perhaps for each timestamp unit or perhaps give it a time window.
#   if time window - for how long? - Could do an hour snapshots
#
# 2. Put the adjency matrices into a dict, where the key is the index of the window and val is the adjency matrix
#
# what kind of data strucure should the dictionary key be? 
# I assume it would be numpy 2d array, right?