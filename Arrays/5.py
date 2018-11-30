#Given two strings, write a function to check if they are one edit (or zero edits) away.

str1 = "pale"
str2 = "babe"

def one_way(str1,str2):
    if (abs(len(str1)-len(str2)) >= 2):
        return False

    m = len(str1)
    n = len(str2)

    count = 0
    i = 0
    j = 0
    while i < m and j < n:
        if str1[i] != str2[j]:
            if count == 1:
                return False

            if m > n:
                i += 1
            elif n > m:
                j += 1
            else:
                i+=1
                j+=1
            count += 1
        else:
            i +=1
            j +=1

    if i < m or j < n:
        count +=1 
    if count == 1:
        return True
    return False

print(one_way(str1,str2))