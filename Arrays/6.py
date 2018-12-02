#Implement a method to perform basic string compression 
#using the counts of repeated characters.

#str1 = "aaabbbcccAAAfffg"
#str1 = "ab"
#str1 = "aabb"
#str1 = "aabcccccccfjkjklllllzzy"
#str1 = "aaabbcccccddd"
str1 = "aaaaa"

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
            finstr += str(count)
            count = 1
            prev = str1[i]
        i = i+1
    finstr += prev
    finstr += str(count)

    if len(str1) <= len(finstr):
        return str1
    return finstr

print(compress(str1))