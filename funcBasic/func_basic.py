# *arguments 是元组；**keywords 是dict
def func1(kind, *arguments, **keywords):
    print("Kind argument is:", kind, "?")
    for arg in arguments:
        print("*argument is :", arg)
    for kw in keywords:
        print(kw, ":", keywords[kw])
    print(list(keywords))
def func2(voltage, state="a stiff", action="voom", type="Blue"):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


if __name__ == "__main__":
    func1("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
    func2('a million', 'bereft of life', 'jump')