import networkx as nx
from numpy import linalg as LA

def define_laplacian(A):
    return nx.laplacian_matrix(A)

def eig_value(A):
    return LA.eig(A)

def eigh_value(A):
    return LA.eigh(A)

def eigvals_value(A):
    return LA.eigvals(A)

def eigvalsh_value(A):
    return LA.eigvalsh(A)

def eig(A, eig_call):
    A_laplace = define_laplacian(A)
    switcher = { 
        "eig": eig_value(A), 
        "eigh": eigh_value(A), 
        "eigvals": eigvals_value(A), 
        "eigvalsh": eigvalsh_value(A)
    }
    return switcher.get(eig_call, eig_value(A))