first_number=input("Enter first number:")
a=int(first_number)
operator=input("Enter operator:")
second_number=input("Enter second number:")
b=int(second_number)
if operator == '+':
        print(a+b)
elif operator == '-':
        print(a-b)
elif operator == '*':
        print(a*b)
elif operator == '/':
        print(a/b)
elif operator == '%':
        print(a%b)
elif operator == '//':
        print(a//b)
elif operator == '**':
        print(a**b)
else:
        print("Invalid operator")
