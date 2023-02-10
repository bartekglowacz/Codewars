"""
The goal of this exercise is to convert a string to a new string where each character
in the new string is "(" if that character appears only once in the original string, or ")"
if that character appears more than once in the original string.
Ignore capitalization when determining if a character is a duplicate.
Examples:
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))(("
"""
import string

print("Wprowadź słowo")
word = input()
signs_list = []


def duplicate_encode(arg):
    arg = arg.casefold()
    for x in arg:
        counter = arg.count(x)
        if counter == 1:
            x = "("
            signs_list.append(x)
        if counter > 1:
            x = ")"
            signs_list.append(x)

    # print("Lista: ", signs_list, "długość: ", len(signs_list))
    signs = "".join(signs_list)
    print(signs, len(signs))
    return signs


duplicate_encode(word)

# print("\nwywołanie funkcji: ", duplicate_encode(word), "długość: ", len(duplicate_encode(word)))
# print(duplicate_encode(word), len(duplicate_encode(word)))
# print(duplicate_encode(word), len(duplicate_encode(word)))
# print(duplicate_encode(word), len(duplicate_encode(word)))
