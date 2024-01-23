# # leetcode 2696

# class Solution(object):
#     def minLength(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         s=list(s)
        
#         print(s)
        
#         while not('AB' in s or 'CD' in s) :
#            return len(s)
              

#         for i in range(len(s)):
#             if i+1<len(s):
#              if (s[i] =='A'  and s[i+1]=='B') or (s[i] =='C' and s[i+1]=='D') :
#                 s.pop(i)
#                 i-=1
#                 s.pop(i+1)
#         print("sss",s)        
#         self.minLength(s)
        
# l= "ABFCACDB"   
# c=Solution()
# c.minLength(l)    



# def s(**kwargs):
#     s1 = 0
#     for key, value in kwargs.items():
#         s1 += value
#     print(s1)

# s(n1=1, n2=2, n3=3, n4=45)

# def s1(*ar):
#     s1=0
#     for i in ar:
#         s1+=i
#     print(s1)   
# s1(1,2,3,4,5)     
# s="ABFCACDB"
# def f(s):
#     while 'AB' in s or 'CD' in s:
#         if 'AB' in s:
#             s=s.replace('AB',"")
#         if 'CD' in s:
#             s=s.replace('CD',"")
#     print(s)    
#     return len(s)     


# f(s)


# class Solution(object):
#     def accountBalanceAfterPurchase(self, purchaseAmount):
#         """
#         :type purchaseAmount: int
#         :rtype: int
#         """

#         li=list(str(purchaseAmount))
#         s=int(li[0])
#         if len(li)>2:
#             x=int(li[1])%10
#         else:
#             x= int(li[0])%10 
     
#         if x>=5:
#             s=(int(li[0])+1)*10
#         else:
#             s=int(li[0])*10
#         print(100-s)    
#         return 100-s

# o=Solution()
# o.accountBalanceAfterPurchase(7)          

# def fn(a):
#     return lambda x:x*a
# x=fn(5)
# print(x(3))
# li=[]
# for i in (1,2,3):
#     li.append(lambda x=i:x)
# for j in li:
#         print(j())  

import time
import asyncio
async def start():
    print("start")
    await asyncio.sleep(3)
    print("finished1")

async def start2():
    print("start2")
    await asyncio.sleep(5)
    print("finished2")

async def main():
    sttime=time.time()
    starts=asyncio.create_task(start())
    strt=asyncio.create_task(start2())
    r1=await starts
    r2=await strt
    endtime=time.time()

    x=endtime-sttime
    print (f"start:{sttime}",f"end:{endtime}",f"timetaken:{x}")    
asyncio.run(main())