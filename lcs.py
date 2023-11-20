def lcs(A, B): 
    a, b = len(A), len(B)
    x = [[0] * (b + 1) for _ in range(a + 1)]
    parent = {}
    for i in reversed(range(a)):
        for j in reversed(range(b)):
            if A[i] == B[j]:
                x[i][j] = x[i + 1][j + 1] + 1 #the reason for the size of x 
                parent[(i, j)] = (i + 1, j + 1) #storing parent pointers for lcs printing
            elif x[i + 1][j] > x[i][j + 1]:
                x[i][j] = x[i + 1][j]
                parent[(i, j)] = (i + 1, j)
            else: 
                x[i][j] = x[i][j + 1]
                parent[(i, j)] = (i , j + 1)
    lcs = ''
    here = (0, 0)
    while i != a - 1 and j != b - 1: #O(a + b) by the definition of the DAG
        i = here[0]
        j = here[1]
        if A[i] == B[j]:
            lcs += A[i]
        here = parent[here]
        print(here)
    return lcs #for lcs print
    #return x[0][0] #for lcs length 

if __name__ == "__main__":
    import random
    import string

    def get_random_string(length):
        #choose from all lowercase letter
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str

    A = 'their'
    B = 'habit'
    print(lcs(A, B))