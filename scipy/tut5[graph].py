from scipy.sparse.csgraph import connected_components
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix
import numpy as np
shared=np.array([[0,1,2],[1,0,0],[2,0,0]])
sharnew=csr_matrix(shared)
# print(sharnew)    
# print(connected_components(sharnew))
print(dijkstra(sharnew, return_predecessors=True, indices=1))