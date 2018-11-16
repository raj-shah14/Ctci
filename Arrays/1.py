string1 = "asdfknerlg"
string2 = "m,dbnjgdboceang"
string3 = ",./';][]./[./"


#With Data structures
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

#Without Data Structures
def isUnique2(string):
    if len(string)> 128:  #Assuming ASCII character set of 128
        return False
    
    char_set = [False for _ in range(128)]
    for i in string:
        val = ord(i)

        if char_set[val]:
            return False
        char_set[val] = True
    return True

print(isUnique2(string1))
print(isUnique2(string2))
print(isUnique2(string3))