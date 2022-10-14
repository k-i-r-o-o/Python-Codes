class Solution:
    def isHappy(self , n: int) -> bool:
        s=lambda n: sum(int(d)**2 for d in str(n))
        m =s(n)
        while m!=n:
            n,m=s(n),s(s(m))
        return n==1
obj=Solution()
print(obj.isHappy(11))

