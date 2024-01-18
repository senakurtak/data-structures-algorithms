from data_st import stack

query = "{[qqq{(aasdc)}asdd]}"
query1 = "{qqq{(aasdc)}asdd]}"
query2 = "{[qqq{(aasdc}asdd]}"
query3 = "{[qqq{(aasdc)asdd]}"

def checkParenthesis(query: str):
    st = stack()
    for letter in query:
        if letter == "(" or letter == "[" or letter == "{":
            st.push(letter)
        elif letter == ")":
            if not st.pop() == "(":
                return False
        elif letter == "]":
            if not st.pop() == "[":
                return False
        elif letter == "}":
            if not st.pop() == "{":
                return False
    if not st.isEmpty():
        return False
    return True

print(checkParenthesis(query))

print(checkParenthesis(query1))

print(checkParenthesis(query2))

print(checkParenthesis(query3))
