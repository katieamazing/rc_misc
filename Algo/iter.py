def foo(iterable):
    return iter(iterable)

def bar(iterator):
    return list(iterator)

def baz(iterable):
    for c in iterable:
        if c.isalpha():
            yield c


print(bar(foo("hello world")))
print(bar(baz("hello world")))


def fizzbuzz():
    i = 0
    x = None
    thing = True
    while thing:
        if i % 15 == 0:
            x = "fizzbuzz"
        elif i % 5 == 0:
            x = "buzz"
        elif i % 3 == 0:
            x = "fizz"
        else:
            x = str(i)
        yield x
        i = i + 1

def fizzbuzz_all_the_yields():
    i = 0
    x = None
    thing = True
    while thing:
        if i % 15 == 0:
            yield "fizz"
            yield "buzz"
        elif i % 5 == 0:
            x = "buzz"
        elif i % 3 == 0:
            x = "fizz"
        else:
            x = str(i)
        yield x
        i = i + 1

def hundo(iterator):
    for x in range(50,100):
        print(next(iterator))

hundo(fizzbuzz_all_the_yields())
