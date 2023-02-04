import random


def even_or_odd(numb):
    if numb % 2 == 0:
        return print("Even")
    if numb % 2 != 0:
        return print("Odd")


number = random.randint(-9, 9) * random.randint(-9, 9)
print(number)
even_or_odd(number)

# end