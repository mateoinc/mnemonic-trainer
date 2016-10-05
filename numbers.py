import random, pickle, sys

Lists = {}
Lists = pickle.load(open("Lists.p" , "rb"))
    

def createList(name,length,minimum,maximum):
    list = []
    for i in range(0, int(length)):
        list.append(random.randint(minimum, maximum))
    global Lists
    Lists[name] = list

def listToString(name):
    list = ""
    for i in Lists[name]:
        if i >= 10:
            list += str(i)
        if i <= 9:
            list += ("0" + str(i))
    return(list)

def checkList(name):
    list = input("Input number to compare\n")
    if list == listToString(name):
        print("Yay! \n")
              
    else:
        print(":( \n The real value was: \n" + listToString(name))


while True:
    global Lists
    print("Input optione: \n")
    print("(1) Create random list\n")
    print("(2) See lists \n")
    print("(3) Check list from memory \n")
    print("(4) Save and Exit \n ")
    try:
        choice = int(input())
    except ValueError:
        print("Error: Input a number, please\n")
        choice = 0
    if choice == 1:
        name = input("Input new list name\n")
        length = (int(input("How many digits will it have?\n")))/2
        minimum = int(input("What is the minimum value to be generated?\n"))
        maximum = int(input("What is the maximum value to be generated?\n"))
        createList(name,length,minimum,maximum)
        print(listToString(name))
    elif choice == 2:
        print(Lists.keys())
    elif choice == 3:
        name = input("Input list name: \n")
        checkList(name)
    elif choice == 4:
        pickle.dump(Lists, open("Lists.p","wb"))
        quit()
    else:
        print("Error: not a valid option \n")

