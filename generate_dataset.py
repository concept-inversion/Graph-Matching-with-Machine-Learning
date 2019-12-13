import random

def generate(Z1):
    i = 0
    while i < len(Z1)-1:
        j = i+1
        edge_count = 0
        print('printing length of Z1',len(Z1))
        while j < len(Z1):
            if Z1[i,j] == 1:
                edge_count+=1
            j+=1
        print(edge_count)
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
        print('changed indexes'+str(changed_indexes))
    l = 0
    while l < len(Z1):
        print(Z1[l])
        l+=1
    return Z1