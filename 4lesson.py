#calculator program
#+ - * / 
print("Press 1 : For add")
print("Press 2 : For subtract")
print("Press 3 : For multiply")
print("Press 4 : For Divide")
userInput= int(input("Please enter something :")) 
print(userInput)
print(type(userInput))

firstNumber= int(input("Please enter First number:"))
secondNumber= int (input("Please enter Second number:"))
if userInput == 1:
    result=firstNumber+secondNumber
elif userInput == 2:
    result=firstNumber-secondNumber
elif userInput == 3:
    result = firstNumber*secondNumber
elif userInput == 4:
    result=firstNumber/secondNumber
else:
    print('You must enter 1/2/3/4:')
print("The number of {} {} {} is {}  ".format(firstNumber,userInput,secondNumber,result))