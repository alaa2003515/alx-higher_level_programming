import sys

if len(sys.argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)

num1 = int(sys.argv[1])
operator = sys.argv[2]
num2 = int(sys.argv[3])

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 == 0:
        print("Error: division by zero")
        sys.exit(1)
    result = num1 / num2
else:
    print("Unknown operator. Available operators: +, -, *, /")
    sys.exit(1)

print(f"{num1} {operator} {num2} = {result}")
