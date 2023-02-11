"""
Usually when you buy something, you're asked whether your credit card number,
phone number or answer to your most secret question is still correct.
However, since someone could look over your shoulder, you don't want that shown on your screen.
Instead, we mask it.

Your task is to write a function maskify, which changes all but the last four characters into '#'.

Examples
"4556364607935616" --> "############5616"
     "64607935616" -->      "#######5616"
               "1" -->                "1"
                "" -->                 ""

// "What was the name of your first pet?"

"Skippy" --> "##ippy"

"Nananananananananananananananana Batman!"
-->
"####################################man!"
"""


print("Wprowadź numer/hasło")
password = input()
# return masked string
def maskify(cc):
    # if len(password) > 4:
    #     last = password[-4:]
    #     first_x = ["#" for x in password[:-4]]
    #     first_x = "".join(first_x)
    #     final = first_x + last
    #     print("Finalnie: ", final)
    # if len(password) < 4:
    #     last = password
    #     final = last
    #     print("Finalnie: ", final)
    #
    # return final
    return "#" * (len(cc) - 4) + cc[-4:]

print(maskify(password))