from data_st import stack
"(3+5*7)-4" # human readable - infix 
ex = "357*+4-"# postfix
"-+*5734"
def postfixCalculation(expression):
    st = stack()
    for letter in expression:
        if not letter in ["+", "-", "*", "/"]:
            st.push(letter)
        else:
            op2 = int(st.pop())
            op1 = int(st.pop())
            if letter == "+":
                st.push(str(op1 + op2))
            if letter == "-":
                st.push(str(op1 - op2))
            if letter == "*":
                st.push(str(op1 * op2))
            if letter == "/":
                st.push(str(op1 / op2))
    return st.pop() # son elemanı return ederek işlemi hesaplar
res = postfixCalculation(ex)
print(res)