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
