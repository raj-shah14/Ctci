#Given a string, write a function to check if it is a permutation of a palindrome.

inp = "carerac"
inp2 = "code"
inp3 = "Tact Coa"

def palinperm(inp):
    temp = {}
    for i in inp:
        if i != ' ':
            if i not in temp:
                temp[i] = 1
            else:
                temp[i] -= 1
    tempsum = 0
    for i in temp.values():
        tempsum += i
    if tempsum == 0 or tempsum == 1:
        return True
    return False
print(palinperm(inp2.lower()))


#solution 2
#Using bit vector
def bitpalinper(inp):
    alpha = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
    arr = [0 for _ in range(26)]
    for i in inp:
        if i != ' ':
            if i in alpha:
                if(arr[alpha[i]] == 0):
                    arr[alpha[i]] = 1
                elif(arr[alpha[i]] == 1):
                    arr[alpha[i]] = 0 
    if sum(arr) == 0 or sum(arr) == 1:
        return True
    return False
print(bitpalinper(inp2.lower()))
