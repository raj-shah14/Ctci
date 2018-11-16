string1 = "raaaj"
string2 = "ajara"

def checkPerm(string1,string2):
    if len(string1) != len(string2):
        return False

    temp = {}

    for i in string1:
        if i not in temp:
            temp[i] = 1
        else:
            temp[i] +=1
    
    for i in string2:
        if i in temp:
            temp[i] -= 1

    print(temp)

print(checkPerm(string1,string2))