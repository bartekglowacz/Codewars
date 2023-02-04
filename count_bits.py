import random


def count_bits(decimal_form):
    binary_form = bin(decimal_form).removeprefix("0b")
    print(binary_form)
    suma = 0
    if decimal_form >= 0:
        for x in binary_form:
            if x == "1":
                suma += 1
        print(f"suma bitowa: {suma}")
        return suma
    else:
        print("input should be a non-negative integer")
        return 0


number = random.randint(-9, 9) * random.randint(-9, 99)
print(number)

count_bits(number)

# end