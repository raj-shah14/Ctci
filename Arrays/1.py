string1 = "asdfknerlgn"
string2 = "m,dbnjgdboceang"
string3 = ",./';][]./[./"

def isUnique(string):
    unwanted = ",./;'[]\<}>?:{+*-!@#$%^&()"

    temp_dict = {}
    for i in string:
        if i in unwanted:
            return False
        if i not in temp_dict:
            temp_dict[i] = 1
        else:
            return False
    return True

print(isUnique(string1))
print(isUnique(string2))
print(isUnique(string3))