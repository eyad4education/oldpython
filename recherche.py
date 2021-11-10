valid = False
while valid == False:
    n = int(input("Entrer n:"))
    valid = n in [2, 20]
T = n*[""]


def minimum(T, n):
    min = T[0]
    for i in range(1, n):
        if T[i] < min:
            min = T[i]
    return min


def maximum(T, n):
    max = T[0]
    for i in range(1, n):
        if T[i] > max:
            max = T[i]
    return max


a = int(input("Entrer a: "))
b = int(input("Entrer b: "))
min = minimum(a, b)
max = maximum(a, b)
print(min, max)
