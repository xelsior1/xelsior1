print("input type of verb: ")
print("ar, er, ir")
i = input()
print("input word: ")
word = input()

def ar():
    print(word + "o")
    print(word + "as")
    print(word + "a")
    print(word + "an")
    print(word + "amos")
def er():
    print(word + "o")
    print(word + "es")
    print(word + "e")
    print(word + "en")
    print(word + "emos")
def ir():
    print(word + "o")
    print(word + "es")
    print(word + "e")
    print(word + "en")
    print(word + "imos")
if i == "ir":
    ir()
elif i == "ar":
    ar()
elif i == "er":
    er()


