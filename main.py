
# function to check if balanced or not
def check_balanced(s):
    # put the input in a list
    list1 = []

    for char in s:
        if char in ["(", "{", "["]:
            # push the char in the list
            list1.append(char)
        # if the current char is not any of the mentioned before (opening char)
        # then they must be a closing char
        else:
            if not list1:
                return False
            current_char = list1.pop()
            if current_char == "(":
                if char != ")":
                    return False
            if current_char == "{":
                if char != "}":
                    return False
            if current_char == "[":
                if char != "]":
                    return False
    # check if list is empty or not
    if list1:
        return False
    else:
        return True


# input from user
s = input(print("enter Input here: "))
if check_balanced(s):
    print("Balanced")
else:
    print("unbalanced")
