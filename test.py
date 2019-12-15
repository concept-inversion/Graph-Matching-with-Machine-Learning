import networkx as nx
import numpy as np
from generate_dataset import *
from process_data import preprocess
from eigen import eig, define_laplacian
from scipy import spatial
from similarity_algorithms import euclidean_distance
from scipy.spatial import distance


def positive_samples_test():
    Z = []
    #sample number in DD.mat dataset
    x = 2
    i = 0
    # i defines the number of samples variations we want to create for a matrix
    while i < 20:
        #append the xth Adj matrix from dataset
        Z.append(preprocess(x))
        i+=1
    # starting to make variations to all matrix except first one
    j = 1
    while j < 20:
        #generate negative/positive samples and modify the Z[j] matrix
        #generate_negative(Z[j])
        generate_negative(Z[j])
        j+=1

    i = 0
    #comparing with all negative matrices
    j = 1
    while j < 20:
        
        Z1_x = nx.from_numpy_matrix(Z[i])
        Z2_x = nx.from_numpy_matrix(Z[j])
        
        # compute the laplacian and eigen values 
        lap1=eig(Z1_x, "eigvalsh")
        lap2=eig(Z2_x, "eigvalsh")
        #import ipdb; ipdb.set_trace()
        
        
        
        print('Variation {} - {}'.format(j, 1 - spatial.distance.cosine(lap1,lap2)))
        print('Variation {} - {}'.format(j, distance.euclidean(lap1,lap2)))
        print('Variation {} - {}'.format(j, distance.minkowski(lap1,lap2)))
        j+=1

positive_samples_test()