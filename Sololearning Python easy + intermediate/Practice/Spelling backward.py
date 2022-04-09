# given a string as input, use recursion to output each letter of the string in reverse order, on a new line
def spell(name):
    name = list(name)
    reverse = name[::-1]
    for i in reverse:
        print(i)

txt = str(raw_input("What is the word?"))
spell(txt)

