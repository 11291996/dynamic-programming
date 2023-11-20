b = {}
def bowling(x):
    n = len(x)
    for i in (n+2, n+1, n):
        x.append(0)
        b[i] = 0
    for i in reversed(range(n)):
        b[i] = max([b[i+1]+x[i], b[i+2] + x[i] * x[i+2]])
    return b[0]

if __name__ == "__main__":
    import random
    x = random.sample(range(-500,500),1000)
    print(bowling(x))