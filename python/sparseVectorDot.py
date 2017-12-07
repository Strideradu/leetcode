def sparsevector(a, b):
    result = 0
    i = 0
    j = 0
    while (i < len(a)and j < len(b)):
        if a[i][0] < b[j][0]:
            i+=1
        
        elif a[i][0] > b[j][0]:
            j+=1

        elif a[i][0] == b[j][0]:
            result += a[i][1] * b[j][1]
            i+=1
            j+=1

    return result