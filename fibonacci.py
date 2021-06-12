#to find fib upto n
'''
def fib(n):
      a=0
      b=1
      print(a,b,end=" ")
      i=2
      while i<n:
            a,b=b,a+b
            print(b,end=" ")
            i+=1
n=int(input())
fib(n)
'''
#sum of fib
'''
def fib(n):
      a=0
      b=1
      #Sum=1
      #print(a,b,end=" ")#0 1
      i=2
      while i<n:
            a,b=b,a+b# 1  1 1 2 2 3
            i+=1
      #print(b)
      Sum=b-1
      print(Sum)
            #Sum=Sum+b#1 2 3....
      
      #print("\nsum=",Sum)
      
      
n=int(input())
fib(n+2)
'''
'''#fibonacci sum using mathematics
def fibsum(n):
      ans=((1+5**0.5)/2)**n-((1-5**0.5)/2)**n#1+
      ans=int(ans/(5**0.5))
      return ans-1
print(fibsum(int(input())+1))#5+1 6
'''
#to print nth fibonacci no#0 1 1 2 3 5 8
'''
def fib(n):
      a=0
      b=1
      i=2
      while i<n:
            a,b=b,a+b
            i+=1

      return(b)      
n=int(input())
print(fib(n))
''' 
#recursion: a func calling it self in def is called recursion
'''

def fib(n):
      if n==1:
            return 0
      elif n==2:
            return 1
      else:
            return(fib(n-1)+fib(n-2))#or fib(n+2)+fib(n+1)
n=int(input())
print(fib(n))
'''
#factorial of a number num
'''
def fact(n):
      fact=1
      for i in range(1,n+1):
            fact=fact*i
            print(fact)
fact(int(input()))
'''
#recursion using factorial
'''
def fact(n):
      if n==0 or n==1:
            return 1
      else:
            return(n*fact(n-1))
print(fact(int(input())))
'''


#nearest before fibonacci if n fib: print fib or else print before fib
'''
def nearbeffib(n):
      a=0
      b=1
      while n>=b:#13>1
            a,b=b,a+b#8 13
      print(a)

n=int(input())
nearbeffib(n)
'''
#nearest after fib if fib is n print(n)
'''
def nearafterfib(n):
      a=0
      b=1
      while n>b:#13>21
            a,b=b,a+b#8 13
      print(b)

n=int(input())
nearafterfib(n)
'''
#nearest fibonacci no
'''
def nearfib(n):
      a=0
      b=1
      print(a,b)
      while n>=b:#13>1
            a,b=b,a+b#8 13
            print(a,b)
      if abs(a-n)<=abs(b-n):
            return a
      else:
            return b

n=int(input())
print(nearfib(n))
'''




















