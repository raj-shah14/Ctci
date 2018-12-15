#Assume you have a method isSubstring which checks if one word is a substring of another



s1 = "waterbottle"
s2 = "erbottlewat"


def rotate(s1):
    s1=list(s1)
    temp = s1[0]
    for i in range(len(s1)-1):
        s1[i] = s1[i+1]

    s1[len(s1)-1] = temp
    return ''.join([i for i in s1])

def isSubstring(s1,s2):
    for i in range(len(s1)):
        if (s1 == s2):
            return True
        s1 = rotate(s1)
        # print(s1)

print(isSubstring(s1,s2))