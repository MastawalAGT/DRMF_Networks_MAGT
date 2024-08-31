import numpy as np 
import scipy.io
import scipy.stats as st
import scipy.integrate
# import networkx as kx
# from libpysal import weights
# import matplotlib.pyplot as plt
# import shapely.geometry as sh
import warnings
warnings.filterwarnings("ignore")

"""
weight_adj computes the weighted adjacency matrix for a 2d conducting network

Paramaters : 
    coordinates : a 2d array of x and y coordinates, of dimension (n,2) where n is the number of points 
    in the graph 
    adjacency_matrix : the adjacency_matrix of the graph 

Returns : 
    weighted_matrix : weighted adjacency matrix of the graph

Local Var: 
    n_node : number of nodes in the graph 
    x : 1d array of x coordinates 
    y : 1d array of y coordinates 
    dx : intermediary matrix involved in pointwise distance calculation using x coords
    dy : intermediary matrix involved in pointwise distance calculation using y coords
    dr : weighted adjacency matrix where dr_ij is the distance between the connected points i and j 
    conductances : conductances_ij is the conductance between the connected points i and j 
    (division by 100 is a theoretical proportion of conductances to length)
    weighted_matrix : weighted_matrix_ij is the conductance between the connected points i and j
"""

def weight_adj(coordinates, adjacency_matrix):
    
    n_node = np.shape(coordinates)[0] 
    x = np.reshape([row[0] for row in coordinates],(n_node,1))
    y = np.reshape([row[1] for row in coordinates],(n_node,1))

    dx = x @ np.ones((1,n_node)) - np.ones((n_node,1)) @ x.transpose() 
    dy = y @ np.ones((1,n_node)) - np.ones((n_node,1)) @ y.transpose()

    dr = np.sqrt(dx**2 + dy**2)
    
    conductances = dr/100
    
    weighted_matrix = adjacency_matrix / conductances
    
    for i in range(n_node):
        weighted_matrix[i,i] = 0 # needed to set the nan_valyes to zero 

    return weighted_matrix

"""
degree_entropy calculates the entropy of the degree probability distrobution calculated from the graph 

Parameter : 
    adjacency_matrix : the adjacency matrix of the graph

Returns : 
    the entropy of the degree probability distrobution calculated from the graph

"""
def degree_entropy(adjacency_matrix): 
    
    degrees = adjacency_matrix.sum(axis = 0)
    
    degree_distrobution = np.histogram(degrees, bins = adjacency_matrix.shape[0], density=True)[0]

    return st.entropy(degree_distrobution) 

"""
edge_entropy calculates the entropy of the edge length by treating the edge length values as a sampling 
from some theoretical continous distrobution. The zero values are ignored as 0 entries in the graph note 
an absence of an edge.

Parameter : 
    adjacency_matrix : the adjacency matrix of the graph

Returns : 
    the entropy of the degree probability distrobution calculated from the graph

"""

def edge_entropy(weighted_matrix):
    weights = weighted_matrix.flatten()

    weights = weights[weights!=0]  

    return st.differential_entropy(weights)

"""
resistance calculates the effective resistance of a 2d conducting network assuing current flows from the 
upper left most corner to the bottom right most corner

Paramaters : 
    coordinates : a 2d array of x and y coordinates, of dimension (n,2) where n is the number of points 
    in the graph 
    adjacency_matrix : the adjacency_matrix of the graph 

Returns : 
    effective_resistance : weighted adjacency matrix of the graph
"""

def resistance(coordinates, adjacency_matrix):
    current = 1 
    n_node = np.shape(coordinates)[0] 
    weighted_matrix = weight_adj(coordinates, adjacency_matrix)
    diag = np.diag(np.sum(weighted_matrix, axis = 1))
    Amat = diag - weighted_matrix
    Amat = Amat[:-1,:-1]
    Ivec = np.zeros((n_node-1,1))
    Ivec[0] = current 
    voltage = np.linalg.solve(Amat, Ivec)
    effective_resistance = voltage[0,0] / current
    return effective_resistance

"""
WARNING: the many of the capabilities that this function utilizes are depreciated and should not be used;
it is only here because of records
"""

# def graph_draw(point_cloud):
    
#     delaunay = weights.Voronoi(point_cloud, criterion='rook', clip=sh.box(0,0,2000,2000))
    
#     graph = delaunay.to_networkx() 
     
#     positions = dict(zip(graph.nodes, point_cloud))
    
#     Fignewton = plt.axes(aspect = "equal")
    
#     kx.draw(graph,positions,ax = Fignewton,node_size=5,node_color="k",edge_color="k",alpha=1,width = 3)
#     plt.show()