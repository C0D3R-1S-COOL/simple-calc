#TODO:
#Add better way to input equations

def arithmetic(operation, number1, number2):
  if operation == "M":
    return number1 * number2
  elif operation == "D":
    return number1 / number2
  elif operation == "A":
    return number1 + number2
  elif operation == "S":
    return number1 - number2
  else:
    raise Exception("Sorry, you enetered an invalid value or operation.")


Number1 = float(input("Enter number 1: "))
operationInput = input("Enter an operation (M - Multiplication, D - Division, A - Add, S - Subtract): ")
Number2 = float(input("Enter number 2: "))
answer = arithmetic(operationInput, Number1, Number2)
print(answer)

useLastAnswer = input("Do you want to reuse the last input in a new operation? (Y - Yes, N - No): ")

while useLastAnswer == "Y":
    Number1 = answer
    operationInput = input("Enter an operation (M - Multiplication, D - Division, A - Add, S - Subtract): ")
    Number2 = float(input("Enter number 2: "))
    answer = arithmetic(operationInput, Number1, Number2)
    print(answer)
    useLastAnswer = input("Do you want to reuse the last input in a new operation? (Y - Yes, N - No): ")
