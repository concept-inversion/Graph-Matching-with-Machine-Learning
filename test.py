import networkx as nx
from generate_dataset import generate
from process_data import preprocess
from eigen import eig, define_laplacian
from scipy import spatial


def positive_samples_test():
    Z = []
    i = 0
    # i defines the number of graph that we want to test from the D&D dataset
    while i < 2:
        Z.append(preprocess(i))
        #print(Z[i])
        i+=1
    j = 1
    while j < 2:
        generate(Z[j])
        print(Z[j])
        j+=1

    Z_x = []
    similarity = []
    i = 0
    while i < 20:
        j = i+1
        while j < 20:
            
            Z1_x = nx.from_numpy_matrix(Z[i])
            Z2_x = nx.from_numpy_matrix(Z[j])
            
            # compute the laplacian and eigen values 
            lap1=eig(Z1_x, "eig")
            lap2=eig(Z2_x, "eig")
            #lap1=nx.spectrum.laplacian_spectrum(Z1_lap)
            #lap2=nx.spectrum.laplacian_spectrum(Z2_lap)
            #import ipdb; ipdb.set_trace()
            
            
            
            print(1 - spatial.distance.cosine(lap1,lap2))
            j+=1
        i +=1

positive_samples_test()