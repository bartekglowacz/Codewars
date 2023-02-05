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

alphabet = "qwertyuiopasdfghjklzxcvbnm"
alphabet_list = list(alphabet)
alphabet_list.sort()

print(alphabet_list)
print("Wprowadź słowo")
word = input()
print(word)
word_list = list(word)

for x in range(0, len(alphabet_list), 1):
    if word_list.count(alphabet_list[x]) != 0:
        print(f"{alphabet_list[x]} -> {word_list.count(alphabet_list[x])}")


