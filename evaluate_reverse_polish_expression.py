def evalRPN(tokens):
    operator_list = ["+","-","*","/"]
    stack = []
    for i in tokens:
        if i not in operator_list:
            stack.append(int(i))
        
        else:
            n1 = stack.pop(-2)
            n2 = stack.pop()
            if i == "+":
                stack.append(n1+n2)
            elif i == "-":
                stack.append(n1-n2)
                
            elif i == "*":
                stack.append(n1*n2)
            elif i == "/":
                stack.append(int(n1/n2))

    return stack


tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

print(evalRPN(tokens))