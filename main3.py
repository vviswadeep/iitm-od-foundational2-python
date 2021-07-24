"""
While Loop

Factorial of a number

n=int(input())
answer =1
while(n!=1):
  answer*=n
  n-=1
print(answer)


Palindrome
num = int(input("Enter a number: "))
PosNum = abs(num)
rev = PosNum % 10
PosNum = PosNum // 10 
while (PosNum>0):
  rem = PosNum % 10
  PosNum = PosNum // 10
  rev = rev * 10 + rem
if(num<0):
  rev = -rev
if(num == rev):
  print("It is a palindrome")
else:
  print("It is not a palindrome")

"""

"""
For Loop 

Hello World 10 times
for i in range(10):
  print(i, "Hellp World")

Sum n terms
num = int(input())
sum=0
for i in range(num):
  sum+=i
print(sum)

tables

for i in range(1,11):
  print("2 x ", i," = ",2*i)
print("------------------")
for i in range(1,11):
  print("3 x ", i," = ",3*i)
print("------------------")
for i in range(1,11):
  print("4 x ", i," = ",4*i)
print("------------------")
for i in range(1,11):
  print("5 x ", i," = ",5*i)
print("------------------")
for i in range(1,11):
  print("6 x ", i," = ",6*i)
print("------------------")


Sort in range-reverse order
for x in range(9,-1,-2):
  print(x)
"""

# #1
# sum=0
# for i in range(1,101):
#   if(i % 2 == 1):
#     sum += i
# print(sum)

# #2
# for j in range(20,0,-1):
#   if (j%2==0):
#     print(j)

# #3
# n = int(input())
# mainans=1
# for j in range(n,1,-1):
#   i=j
#   ans = 1
#   while(i!=1):
#     ans*=i
#     i-=1
#     #print("in",ans)
#   mainans+=ans
#   #print(mainans)
# print(mainans/n)

#4
# total = 0
# n = int(input())
# if (n == 0 or n == 1):
#   total = 0
# if (n == 2):
#   total = 2
# if(n>2):
#   for i in range(3, n):
#     flag = False
#     for j in range(2, i):
#       if (i % j == 0):
#         flag=False
#         break
#       else:
#         flag=True
#     if flag:
#       total = total + i
#   total = total+2
# print(total)

# n = int(input())
# i = 0
# while i < n:
#   j = 0
#   while j < n:
#     if i==j or i+j==n-1 or j == n//2 or i == n//2 or i == 0 or i == n-1 or j == 0 or j == n-1:
#       print('*', sep='', end='')  
#     else:
#       print(' ', sep='', end='')
#     j = j + 1
#   i = i + 1
#   print()

# n = int(input())
# for i in range(1,n):
#   for j in range(i+1,n):
#     for k in range(j+1,n):
#       if i**4 +j**3 == k**2:
#         print(i,j,k)

# a=input()
# b=input()
# out=''
# for i in range(len(a)):
#   for j in range(len(b)):
#     if a[i]==b[j]:
#       continue
#     else:
#       out+=b[j]
#   b = out
#   out=''
# print(b)

# a = int(input())
# out=0
# i=1
# while i<=a:
#   for j in range(1,i+1):
#     out = out+j
#     print(i,j)
#   i+=1
# print(out)


# n = int(input())
# count=1
# if(n>2):
#   for i in range(3, n+1):
#     flag = False
#     for j in range(2, i):
#       if (i % j == 0):
#         flag=False
#         break
#       else:
#         flag=True
#     if flag and n%i ==0:
#       if count<2 and n%2==0:
#         print(2)
#         count+=1
#       print(i)
# if n==2:
#   print(2)

# a = input()
# i = a.lower()
# stri = sorted(list(i))
# for i in stri:
#   if i.isalpha():
#     print(i,end='')

# x=input()
# for i in range(2,len(x)):
#   flag=True
#   for j in range(2,i):
#     if i%j==0:
#       flag=False
#       break
#   if flag==True:
#     print(x[i])

x = 0
x_ = 1
for i in range(10):
  x,x_=x_,x+x_
print(x)

y = 0
y_ = 1
for i in range(10):
  y=y
  y_=y+y_
print(y)