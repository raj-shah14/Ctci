#Implement a method to perform basic string compression 
#using the counts of repeated characters.

#str1 = "aaabbbcccAAAfffg"
#str1 = "ab"
#str1 = "aabb"
str1 = "aabcccccccfjkjklllllzzy"
#str1 = "aaabbcccccddd"
#str1 = "aaaaa"

def compress(str1):
    finstr = ""
    prev = str1[0]
    count = 1
    i = 1
    while i < len(str1):
        if(str1[i] == prev):
            count += 1
        else:
            finstr += prev
            finstr += `count`
            #finstr += str(count)      #Instead of using str, one should use backticks (``)
            count = 1
            prev = str1[i]
        i = i+1
    finstr += prev
    finstr += `count`      #Converts int to string
    #finstr += str(count)

    if len(str1) <= len(finstr):
        return str1
    return finstr

print(compress(str1))  #O(n^2) time complexity 

#Alternate Method using List Comprehension
def compress2(str1):
    finstr = []
    prev = str1[0]
    count = 1
    i = 1
    while i < len(str1):
        if(str1[i] == prev):
            count += 1
        else:
            finstr.append(prev)
            finstr.append(count)
            count = 1
            prev = str1[i]
        i = i+1
    finstr.append(prev)
    finstr.append(count)
    str2 = ''.join([str(num) for num in finstr])

#String Concatenation is a costly operator as it creates a new copy of string and copies old contents
#A fastest approach would be to use list comprehension.


    if len(str1) <= len(str2):
        return str1
    return str2

print(compress2(str1))  #O(n^2) time complexity but slightly better.