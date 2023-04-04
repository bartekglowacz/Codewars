# instrukcja wykonania: https://www.codewars.com/kata/5515395b9cd40b2c3e00116c

def regressionLine(x, y):
    n = len(x)
    suma_x_kwadrat = []
    suma_y = []
    suma_x = []
    suma_xy = []
    for i in range(0, n):
        suma_x_kwadrat.append(pow(x[i], 2))
        suma_x.append(x[i])
        suma_y.append(y[i])
        suma_xy.append(x[i] * y[i])
    suma_x_kwadrat = sum(suma_x_kwadrat)
    suma_x = sum(suma_x)
    suma_y = sum(suma_y)
    suma_xy = sum(suma_xy)
    a = (suma_x_kwadrat * suma_y - suma_x * suma_xy) / (n * suma_x_kwadrat - pow(suma_x, 2))
    b = (n * suma_xy - suma_x * suma_y) / (n * suma_x_kwadrat - pow(suma_x, 2))
    a = round(a, 4)
    b = round(b, 4)
    print(f"{a = }\n{b = }")
    return a, b


x = [25, 30, 35, 40, 45, 50]
y = [78, 70, 65, 58, 48, 42]

regressionLine(x, y)
