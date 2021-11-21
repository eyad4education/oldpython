n=int(input("Entrer un nombre entre 1 et 10: "))
while n<1 or n>10:
    n=int(input("Entrer un nombre entre 1 et 10: "))
m=0
for i in range(1,10):
    m=i*n
    print(i,"x",n,"=",m)
