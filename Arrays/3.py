#URLify a string with %20
inp = "Mr John Smith   "
tl = 13
#inp = " Raj S h a h loves footbal l "
#tl = 28

out = ""
for i in inp:
    if(tl > 0):
        if i != " ":
            out+=i
        else:
            out+="%20"
    tl-=1
print(out)  #O(n) time and O(n) Space

#2nd approach
def urlify(string,tl):
    return ''.join('%20' if c == ' ' else c for c in string[:tl])

print(urlify(inp,13)) #O(n) time and O(n) Space

