import statistics


def distances_from_average(test_list):
    aver_of_numbers = statistics.mean(test_list)
    return [round(aver_of_numbers - value, 2) for value in test_list]


list_of_numbers = []
print("Wprowadź listę liczb. Wpisanie litery kończy wpisywanie")
number = input()

while not number.isalpha():
    list_of_numbers.append(float(number))
    number = input()
print(list_of_numbers)

distance_from_average = distances_from_average(list_of_numbers)
print(distance_from_average)