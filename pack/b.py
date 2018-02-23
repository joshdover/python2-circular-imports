import importlib
a = importlib.import_module('.a', 'pack')


def hi():
    print("hi from b")
    a.hi()
