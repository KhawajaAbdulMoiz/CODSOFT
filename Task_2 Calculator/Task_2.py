def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Division by zero is not acceptable."
    else:
        return x / y
    

print("\n")
print("Choose an Operation")
print("------------------------------------------")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
while True:
    choice=input("Enter choice 1,2,3,4 : \n")

    if choice in ('1','2','3','4'):
        num1=int(input("Enter number 1 : "))
        num2=int(input("Enter number 2 : "))

    if choice=='1':
        print(f"The sum of {num1} and {num2} is :", add(num1, num2))
    elif choice=='2':
        print(f"The difference of {num1} and {num2} is :", subtract(num1, num2))
    elif choice=='3':
        print(f"The product of {num1} and {num2} is :", multiply(num1, num2))
    elif choice=='4':
        print(f"The division of {num1} and {num2} is :", divide(num1, num2))
    else:
        print("Invalid Input")
    repeat = input("Do you want to perform another calculation? (yes/no): ")
    if repeat.lower() != 'yes':
            break
   
