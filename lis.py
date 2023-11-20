from dag_shortest_path import Graph

def lis(A): 
    A.append(max(A) + 1)
    a = len(A)
    x = [0] * a #appended last element's L[i] is counted as 0
    parent = [[0] * (a) for _ in range(a)]
    for i in reversed(range(a)):
        for j in range(i, a):
            if A[j] > A[i]:
                x[i] = max(x[i], 1 + x[j]) #L[i] calculation
                parent[j][i] = 1 #creating DAG

    DAG = Graph(a)
    for k in range(a):
        for l in range(a):
            if parent[k][l] == 1:
                DAG.addEdge(k, l, - 1)
    
    #print(DAG.shortestPath(a - 1))
    #print(x)
    #then as this shows, L[i] represents the longest path in the DAG 

    #finding indice for longest path, same as BFS modified in Data Structure and Algorithms
    b = max(x)
    indice = []
    for m in range(len(x)):
        if x[m] == b:
            indice.append(m)
            b -= 1
    lis = []
    for n in indice:
        lis.append(A[n])
    return lis[:-1] #eliminate the base case #for lis print
    #return max(x) #for lis length 

if __name__ == '__main__': 
    import random
    #A =  [5, 13, 16, 1, 20, 8, 25]
    A = random.sample(range(0,1500),1000)
    print(A)
    print(lis(A))
