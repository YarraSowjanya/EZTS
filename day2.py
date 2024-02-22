#Sugarcane juice
'''
def testcase(t):
        if(t==0):
            return 0
        n=int(input())
        sugarcane(n)
        testcase(t-1)
def sugarcane(n):
    total=50*n
    profit=total-0.7*total
    print(profit)
t=int(input())
testcase(t)
'''
#Watching movies at 2x speed
'''
def movie(a,b):
    print(a-(b//2))
a,b=map(int,input().split())
movie(a,b)
'''
#Lucky four
'''
def testcase(t):
    if(t==0):
        return 0
    count=0
    a=int(input())
    while(a>0):
        rem=a%10
        if(rem==4):
            count=count+1
        a//=10
    print(count)
    testcase(t-1)
t=int(input())
testcase(t)
'''
#Factorial of a number
'''
def fact(n):
    if(n==0 or n==1):
        return n
    else:
        return n*fact(n-1)
n=int(input())
print(fact(n))
'''
#Next even number
'''
n=int(input())
if(n%2!=0):
    print(n+1)
else:
    print(n+2)
'''
#Add 3 left and right of a three digit number
'''
n=int(input())
print(3*10000+(n*10+3))
'''
#add 3 left and right when you don't know digit count
'''
def count(n):
    c=0
    while(n>0):
        rem=n%10
        c+=1
        n//=10
    return c
t=int(input())
n=t*10+3
temp=n
noofdigits=count(n)
first=3*(10**noofdigits)
print(first+n)
'''
#append(Add 3 left and right of a three digit number)
'''
n=int(input())
s=str(n)
print("3"+s+"3")
'''

