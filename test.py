import networkx as nx
import numpy as np
from generate_dataset import *
from process_data import preprocess
from eigen import eig, define_laplacian
from scipy import spatial
from similarity_algorithms import euclidean_distance


def positive_samples_test():
    Z = []
    x = 2
    i = 0
    # i defines the number of samples variations we want to create for a matrix
    while i < 20:
        #append the xth Adj matrix from dataset
        Z.append(preprocess(x))
        print(len(Z[i]))
        i+=1
    # starting to make variations to all matrix except first one
    j = 1
    while j < 20:
        #generate negative samples and modify the Z[j] matrix
        generate_negative(Z[j])
        print(Z[j])
        j+=1

    Z_x = []
    i = 0
    while i < 20:
        j = i+1
        while j < 20:
            
            Z1_x = nx.from_numpy_matrix(Z[i])
            Z2_x = nx.from_numpy_matrix(Z[j])
            
            # compute the laplacian and eigen values 
            lap1=eig(Z1_x, "eigvalsh")
            lap2=eig(Z2_x, "eigvalsh")
            #ap1=nx.spectrum.laplacian_spectrum(Z1_x)
            #lap2=nx.spectrum.laplacian_spectrum(Z2_x)
            #import ipdb; ipdb.set_trace()
            
            
            
            print(1 - spatial.distance.cosine(lap1,lap2))
            print(np.linalg.norm(lap1-lap2))
            j+=1
        i +=1

positive_samples_test()