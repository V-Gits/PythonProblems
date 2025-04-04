def NaturalNumbers(NUM):
    if NUM <= 0:
        return "Input should be a positive integer."
    print(NUM, end = ",")
    NaturalNumbers(NUM - 1)

NUM = int(input('Enter the Number: '))
NaturalNumbers(NUM)