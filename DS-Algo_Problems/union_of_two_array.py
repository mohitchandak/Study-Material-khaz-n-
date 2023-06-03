class Solution:
    def doUnion(self,a,n,b,m):
        arr=[]
        for i in a+b:
            arr.append(i)
        return (len(set(arr)))

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n,m=[int(x) for x in input().strip().split()]
        a=[int(x) for x in input().strip().split()]
        b=[int(x) for x in input().strip().split()]
        ob=Solution()
        print(ob.doUnion(a,n,b,m))