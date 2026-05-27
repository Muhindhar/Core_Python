def word(inp):
    numbers = {"1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine","0":"zero"}
    for i in inp:
        print(numbers[i],end=" ")
inp = input("Enter the number: ")
word(inp)


