a = '1'
b = ''
for i in range(0, 5):
    j = 0
    k = 0
    while j < len(a):
        while k < len(a) and a[k] == a[j]: 
            k += 1
        b += str(k-j) + a[j]
        j = k
    print("output:",b)
    a = b
    b = ''
print(len(a))