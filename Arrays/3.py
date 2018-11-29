#URLify a string with %20
#inp = "Mr John Smith   "
#tl = 13
inp = " Raj S h a h loves footbal l "
tl = 28

out = ""
for i in inp:
    if(tl > 0):
        if i != " ":
            out+=i
        else:
            out+="%20"
    tl-=1
print(out)