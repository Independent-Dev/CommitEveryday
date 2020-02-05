def get_primes(x=2):
    # if x == 2:
    #     yield x
    #     x+=1
    while True:
        for i in range(2, x):
            if x%i==0:
                break
        else:
            yield x
        x+=1

if __name__ == "__main__":
    i = get_primes()
    for c in range(10):
        print(next(i))
