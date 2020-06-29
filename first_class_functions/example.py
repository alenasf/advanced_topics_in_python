"""Example_1"""
def outer():
    def inner():
        print("in inner")
    return inner
# second '()' revoke  inner()
# outer()()

# var to store function
inner_func = outer()
inner_func()


"""Example_2"""
def outer(param):
    def inner():
        print("in inner", param)
    return inner
inner_func = outer("this is outers param")
inner_func()
inner_func2 = outer("another param for outer")
inner_func2()


# """Example_3"""
def outer(param):
    def inner(inner_param):
        print("outer param", param)
        print("in inner", inner_param)
    return inner
inner_func = outer("this is outers param")
inner_func("this is inner param")
inner_func("this is another inner param")


"""Example_4"""
def division(a,b):
    return a/b


def test(first, second, passed_func):
    print(passed_func(first,second))
# pass reference to division.Do not call the func, so do not insert "()"
test(10,5,division)



