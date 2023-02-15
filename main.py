import re

#Get User Input:
def gef_input():
    string = input("Input String: ")
    pattern = input("Input Pattern: ")
    return string, pattern

#Menu Of Command:

def menu(string, pattern):
    while True:
        print("\n Choose Operation:")
        print("1 ~ Find All")
        print("2 ~ Search")
        print("3 ~ Split")
        print("4 ~ Substitute")
        print("5 ~ Exit")

        choose = input("Input Your Choise:")

#Add Functional For Choise:
        if choose == '1':
            matches = re.findall(pattern,string)
            print("Matches Found: ", + matches)
        elif choose == '2':
            matches = re.search(pattern, string)
            if matches:
                print("Matches Found As Index", matches.start())
            else:
                print("ERROR")
        elif choose == '3':
            parts = re.split(pattern, string)
            print("Parts ~ ", parts)
        elif choose == '4':
            substitue = input("Input Replacement: ")
            replace = re.sub(pattern, substitue, string)
            print("Replaced: ", replace)

        elif choose == '5':
            break
        else:
            print("Invalid Syntax")
