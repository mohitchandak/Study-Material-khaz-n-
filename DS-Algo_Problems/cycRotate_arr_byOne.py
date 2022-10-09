def rotate(arr,n):
    x=arr[n-1]
    for i in range(n-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=x
    return arr

def main():
    t=int(input())
    while(t>0):
        n=int(input())
        a=[int(x) for x in input().strip().split()]
        rotate(a,n)
        print(*a)
        t-=1

if __name__=='__main__':
    main()

