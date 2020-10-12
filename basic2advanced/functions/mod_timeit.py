import timeit

def test():
    print('Hello')
    pass


t1 = timeit.timeit("1+1")
print(t1)

t2 = timeit.timeit(test, number=100)
print(t2)
