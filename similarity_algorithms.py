from math import *

# Minkowski distance
def kth_root(value, k): 
    power = 1 / float(k) 
    return round(value ** power, 3)
  
def minkowski_distance(x, y, k):   
    return (kth_root(sum(pow(abs(a-b), k) 
            for a, b in zip(x, y)), k))

def euclidean_distance(x, y):
    return sqrt(sum(pow(a-b,2) for a, b in zip(x, y)))

def manhattan_distance(x, y):
    return sum(abs(a-b) for a, b in zip(x, y))

def cosine_similarity(x, y):
    numerator = sum(a*b for a, b in zip(x, y))
    denominator = square_rooted(x) * square_rooted(y)