def Readf():
    print("Enter Id of record to read\n")
    x= int(input())
    file=open('test.txt')
    lines=file.readlines()
    print(lines[x])
    file.close()


def Writef():
    print("""Start Writing to the file
    in the format of records(ID|Name|Grade)\n""")
    str=input()
    file=open('test.txt','a+')
    file.write(str + "\n")
    file.close()

def Deleteline():
    print("Enter ID to delete")
    l=int(input())
    with open("test.txt", "r") as infile:
        lines = infile.readlines()

    with open("test.txt", "w") as outfile:
        for pos, line in enumerate(lines):
            if pos != l:
                outfile.write(line)
def ReadAll():
    file = open('test.txt', 'r')
    for line in file:
        print(line)
    file.close()

def init():
    print("""Welcome to my file manager! Please Select an operation to perform 
          by entering the corresponding number
           1- Read 
           2- Write
           3- Delete lines
           4- ReadAll the file 
           5- Exit
           """)
    file = open('test.txt','r+')
    file.write("ID|NAME|GRADE\n")
