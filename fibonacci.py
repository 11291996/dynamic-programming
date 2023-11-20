def fibonacci(n):
    if n == 0: 
        return 0
    elif n == 1:
        return 1 
    return fibonacci(n-1)+fibonacci(n-2)

memo = {}
def fibonacci_mem(n):
    if n < 2:
        memo[n] = n
    if n not in memo:
        memo[n] = fibonacci_mem(n-1)+fibonacci_mem(n-2) 
    return memo[n]

if __name__ == "__main__":
    print(fibonacci_mem(450))