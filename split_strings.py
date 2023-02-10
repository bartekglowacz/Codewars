"""Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd
number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
"""
import enum

print("Wpisz słowo")
text = input()


def solution(s):
    text_list = []
    list_tmp = []
    text_list = [str(x) for x in text]
    # print(text_list)
    if len(s) % 2 == 0:
        for x in range(0, len(s), 2):
            list_tmp.append(s[x:x+2])
        print(list_tmp)
    else:
        for x in range(0, len(s), 2):
            list_tmp.append(s[x:x + 2])
        # print(list_tmp)
        # print(len(list_tmp))
        # print(list_tmp[len(list_tmp)-1])
        last_element = list_tmp[len(list_tmp) - 1] + "_"
        # print("Ostatni element: ", last_element)
        list_tmp.remove(list_tmp[len(list_tmp)-1])
        # print(list_tmp)
        list_tmp.insert(len(list_tmp), last_element)
        print(list_tmp)
    return list_tmp


solution(text)
