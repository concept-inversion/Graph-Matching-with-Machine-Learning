import networkx as nx
from numpy import linalg as LA

def define_laplacian(A):
    return nx.laplacian_matrix(A)

def eig_value(A):
    import ipdb; ipdb.set_trace()
    return LA.eig(A)

def eigh_value(A):
    return LA.eigh(A)

def eigvals_value(A):
    return LA.eigvals(A)

def eigvalsh_value(A):
    return LA.eigvalsh(A)

def eig(A, eig_call):
    A_laplace = define_laplacian(A)
    A_laplace = A_laplace.todense()
    switcher = { 
        "eig": eig_value(A_laplace), 
        "eigh": eigh_value(A_laplace), 
        "eigvals": eigvals_value(A_laplace), 
        "eigvalsh": eigvalsh_value(A_laplace)
    }
    return switcher.get(eig_call, eig_value(A_laplace))