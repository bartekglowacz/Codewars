import math


def zeros(n):
    if n > 0:
        kmax = math.floor(math.log(n, 5))
        number_of_zeros = 0
        for k in range(1, kmax + 1):
            number_of_zeros += math.floor(n / (pow(5, k)))
    else:
        number_of_zeros = 0
    return number_of_zeros


n_input = 6
zera = zeros(n_input)
print(zera)
