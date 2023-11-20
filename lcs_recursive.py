def lcs(X, Y, m, n):
    if m == 0 or n == 0:
       return 0
    elif X[m-1] == Y[n-1]:
       return 1 + lcs(X, Y, m-1, n-1)
    else:
       return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n))

if __name__ == "__main__":
    import random
    import string

    def get_random_string(length):
        # choose from all lowercase letter
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str

    X = get_random_string(100)
    Y = get_random_string(100)

    print ("Length of LCS is ", lcs(X, Y, len(X), len(Y)))