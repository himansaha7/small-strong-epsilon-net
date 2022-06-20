inputIntegers = list(map(int, input().split()))
A = inputIntegers[0]
B = inputIntegers[1]
C = inputIntegers[2]

'''if C < A + B:
    #print(C, sep= '', "/", sep= '', A + B)
    print(str(C) + "/" + str(A + B))
else:
    print(str(1) + "/" + str(1))'''

print(str(C ** 2) + "/" + str(A * B * 2))