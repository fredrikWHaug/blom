
def fib(n):
    results = []
    a, b = 0, 1
    while a <= n:
        a, b = b, a + b
        results.append(a)
    return results

def main():
    print(fib(10))

main()