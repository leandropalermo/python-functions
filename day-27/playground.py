def add(*args):
    sum_value = sum(args)
    return sum_value


print(add(4, 3, 8, 9, 2, 2))


# def calculate(**kwargs):
#     print(kwargs)
#     # for key, value in kwargs:
#     #     print(key)
#     #     print(value)
#
#     print(kwargs["add"])
# calculate(add=3, multiply=9)


def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs:
    #     print(key)
    #     print(value)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(4, add=3, multiply=9)

class Car:
    def __init__(self, **kwargs):
        self.model = kwargs.get("model")
        self.make = kwargs.get("make")

my_car = Car(model="Nissan", make="GT-R")
print(my_car.model)
print(my_car.make)

