def main():
    expression = input("Expression: ")
    operand1, operator, operand2 = expression.strip().split()
    match operator:
        case "+":
            print(float(operand1)+float(operand2))
        case "-":
            print(float(operand1)-float(operand2))
        case "*":
            print(float(operand1)*float(operand2))
        case "/":
            if operand2 != '0':
                print(float(operand1)/float(operand2))

main()
