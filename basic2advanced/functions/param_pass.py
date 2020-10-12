
def test(*arg, **kwargs):
    print(*arg)

    print("kwargs:")
    for key, val in kwargs.items():
        print(key, val)


params = ('Li', 34, 'single')
kparams = {'P1': 'param1', 'P2': 'param2'}

test(*params, **kparams)
