import networkx as nx
from generate_dataset import generate
from process_data import preprocess
from eigen import eig
from scipy import spatial


def positive_samples_test(self):
    Z = []
    i = 0
    while i < 20:
        Z.append(preprocess(0))
        print(Z[i])
        i+=1
    j = 1
    while j < 20:
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
            
            lap1=nx.spectrum.laplacian_spectrum(Z1_x)
            lap2=nx.spectrum.laplacian_spectrum(Z2_x)
            #lap1=eig(Z1_x, "eig")
            #lap2=eig(Z2_x, "eig")
            print(1 - spatial.distance.cosine(lap1,lap2))
            j+=1
        i +=1