def get_primes(x=2):
    while True:
        for i in range(2, x):
            if x%i ==0:
                break
            else:
                yield x
            x += 1

if __name__ == "__main__":
    i = get_primes()
    for c in range(10):
        print(c)
        print(next(i))
