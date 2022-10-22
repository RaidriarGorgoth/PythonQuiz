inp = ''
sumhouse = 0


##################################
def QuizQuestions():
    sumhouse = 0
    print("-------------------------")
    print("Q. Pick a favourite class")
    print("a. Charms")
    print("b. Defence against Dark Arts")
    print("c. Transfiguration")
    print("d. History of Magic")

    inp = input("Enter answer : ")
    sumhouse = sumhouse + calculateSum(inp)

    print("-------------------------")
    print("Q. Pick your favourite colour")
    print("a. Yellow")
    print("b. Red")
    print("c. Green")
    print("d. Blue")

    inp = input("Enter answer : ")
    sumhouse = sumhouse + calculateSum(inp)

    print("-------------------------")
    print("Q. What do you do in your free time")
    print("a. Help organise a bake-a-thon")
    print("b. Fight Dragons ")
    print("c. Plot against your colleagues")
    print("d. Visit the Library")

    inp = input("Enter answer : ")
    sumhouse = sumhouse + calculateSum(inp)
    DisplayHouse(sumhouse)


##################################


def calculateSum(i):
    t = 0
    if (i == 'a'):
        t = 1
    elif (i == 'b'):
        t = 3
    elif (i == 'c'):
        t = 4
    elif (i == 'd'):
        t = 2
    return t


##################################


def DisplayHouse(sumhouse):
    if (sumhouse <= 5 and sumhouse >= 0):
        print("Hufflepuff")
    if (sumhouse <= 8 and sumhouse >= 6):
        print("Ravenclaw")
    if (sumhouse <= 11 and sumhouse >= 9):
        print("Gryffindor")
    if (sumhouse >= 12):
        print("Slytherin")
    print(sumhouse)

    print("Thank you for playing")


#####################################
print("Lets Start the Quiz!")
QuizQuestions()
