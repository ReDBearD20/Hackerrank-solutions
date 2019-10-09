from itertools import product
A=set(map(int,input().split()))
B=set(map(int,input().split()))
x=list(product(A,B))

for i in x:
    print(i,end=" ")