
#* if-else, if-elif-else

def if_else(lang):
    if lang == "th":
        print("sawadee")
    else:
        print("hello")

def if_elif_else(lang):
    if lang == "th":
        print("sawadee")
    elif lang == "jp":
        print("konichiwa")
    else:
        print("hello")

#* short hand if-else -> ternary
def ternary_if_else(age):
    return 0 if age <= 5 or age >= 60 else 100

print(ternary_if_else(20))