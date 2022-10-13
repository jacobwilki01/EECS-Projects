#make a function that prints the fibbonacci sequence
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def main():
    fib(2000)

if __name__ == "__main__":
    main()