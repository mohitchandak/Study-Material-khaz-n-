for _ in range(int(input())):
    n=int(input())
    A=list(map(int,input().split()))
    B=A[::-1]
    for i in B:
        print(i,end=" ")
    print("")