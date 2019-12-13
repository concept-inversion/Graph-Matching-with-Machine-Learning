from scipy.io import loadmat
import numpy as np
import networkx as nx
import random
import sys

def preprocess(i):
    original_data = loadmat('datasets/DD.mat', mat_dtype=True)
    import ipdb; ipdb.set_trace()
    Z1=original_data['DD'][0][i][0].todense()
    return Z1
