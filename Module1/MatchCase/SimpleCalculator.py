OPERATOR = input("Enter an Operator out of the following Operators (+,-,x,/,//,%,^): ")
OPERAND1, OPERAND2 = map(int,input("Enter the Operands: ").split(","))

match OPERATOR:
    case "+":
        OPERATION = OPERAND1 + OPERAND2
        print(f"{OPERAND1} + {OPERAND2} = {OPERATION}")
    case "-":
        OPERATION = OPERAND1 - OPERAND2
        print(f"{OPERAND1} - {OPERAND2} = {OPERATION}")
    case "x":
        OPERATION = OPERAND1 * OPERAND2
        print(f"{OPERAND1} x {OPERAND2} = {OPERATION}")
    case "/":
        OPERATION = OPERAND1 / OPERAND2
        print(f"{OPERAND1} / {OPERAND2} = {OPERATION}")
    case "//":
        OPERATION = OPERAND1 // OPERAND2
        print(f"{OPERAND1} // {OPERAND2} = {OPERATION}")
    case "%":
        OPERATION = OPERAND1 % OPERAND2
        print(f"{OPERAND1} % {OPERAND2} = {OPERATION}")
    case "^":
        OPERATION = OPERAND1 ** OPERAND2
        print(f"{OPERAND1} ^ {OPERAND2} = {OPERATION}")
