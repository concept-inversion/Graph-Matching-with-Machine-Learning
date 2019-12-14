import random

def generate_positive(Z1):
    i = 0
    while i < len(Z1)-1:
        j = i+1
        edge_count = 0
        while j < len(Z1):
            if Z1[i,j] == 1:
                edge_count+=1
            j+=1
        changed_indexes = []
        while edge_count != 0:
            random_index = random.randint(i+1, len(Z1)-1)
            if random_index in changed_indexes:
                continue
            changed_indexes.append(random_index)
            Z1[i,random_index] = 1
            Z1[random_index,i] = 1
            edge_count-=1
        k = i+1
        while k < len(Z1):
            if k in changed_indexes:
                k+=1
                continue
            Z1[i,k] = 0
            Z1[k,i] = 0
            k+=1
        i+=1
    return Z1

def generate_negative(Z1):
    #i defines current row being iterated in a matrix
    i = 0
    while i < len(Z1):
        #j defines current column being iterated in a matrix. j is always greater than i because we only care about upper half of the Adj matrix
        j = i+1
        #j(column count) should run till last element
        while j < len(Z1):
            random_value = random.randint(0, 1)
            Z1[i, j] = random_value
            #updating lower half of Adj matrix as soon as upper half element is edited
            Z1[j, i] = random_value
            #before exiting a row iteration, this makes sure that the diagonal element is set to 0
            Z1[i, i] = 0
            j+=1
        i+=1