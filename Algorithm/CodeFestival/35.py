def one(n):
    def two(m):
        return m**n
    return two

if __name__=="__main__":
    a = one(2)
    b = one(3)
    c = one(4)
    print(a(10))
    print(b(10))
    print(c(10))
