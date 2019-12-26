from funs import *

while True:
    init()
    var = int(input())
    if var == 1:
        Readf()
    elif var == 2:
        Writef()
    elif var == 3:
        Deleteline()
    elif var == 4:
        ReadAll()
    elif var==5:
        exit()
    else:
        print("Enter a Valid input")