def solution(text):
    my_string = "".join([s if s.islower() else " " + s for s in text])[1:]
    print(my_string)
    return my_string


text_to_format = "AlaMaKotaAKotMaWpierdol"
solution(text_to_format)