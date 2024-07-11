x = "global"


def outer():
    x = "local"

    def inner():
        # nonlocal can be only used in nested func
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    def change_global():
        # refers to the global scope
        global x
        x = "global: changed!"

    print("outer:", x)
    inner()
    print("outer:", x)
    change_global()


print(x)
outer()
print(x)
