test = [["a","b","c","d","e"],
        ["f","g","h","i","j"],
        ["k","l","m","n","o"],
        ["p","q","r","s","t"],
        ["u","v","w","x","y"]]

def sort_lexo(array):
    return sorted(array)

def get_diag(test):
    max_col = len(test[0])
    max_row = len(test)
    fdiag = [[] for _ in range(max_row + max_col - 1)]
    bdiag = [[] for _ in range(max_row + max_col - 1)]
    min_bdiag = -max_row + 1

    for x in range(max_row):
        for y in range(max_col):
            fdiag[x+y].append(test[x][y])
            bdiag[y-x-min_bdiag].append(test[x][y])

    l = []
    for i in bdiag:
        l.append(("".join(i) * max_row)[:max_row])
    return l



print(sort_lexo(get_diag(test)))

queries = ["+2", "+4", "+5", "+1", "-2"]
ans = []
diff = 1

def binsearch(array, diff, ans):
    count = 0
    array = sorted(array)
    l = 0
    r = len(array) - 1

    while l < r:
        val = array[l] - array[r]
        if val < 0:
            val *= -1
        
        if val == diff:
            count += 1
        if val > diff:
            r -= 1
        else:
            l += 1
    ans = ans + [count]
    return ans

def get_diff(array, diff, ans):
    print(array)
    count = 0
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if i != j:
                val = array[i] - array[j]
                if val < 0:
                    val *= -1

                if val == diff:
                    count += 1
    ans = ans + [count]
    return ans


numbers = []
for i in range(len(queries)):
    if "+" in queries[i]:
        numbers.append(int(queries[i].split("+")[1]))
        #ans = binsearch(numbers, diff, ans)
        ans = get_diff(numbers, diff, ans)
    else:
        numbers.remove(int(queries[i].split("-")[1]))
print(ans)