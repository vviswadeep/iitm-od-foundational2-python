'''
Week 2 Activity Questions
'''

#1
# a=1
# print(type(a))
# a=1.0
# print(type(a))
# a='1'
# print(type(a))

#2
# x, y, z = 3,4,5
# x,y,z =x**2,y**2,z**2 #squares the input
# print(x+y==z)#pytho triplet, condition is checked with == , so answer true

#3
# good_variable = 10
# a_ =1
# _a =2
# 1_a = 10 #wrong declaration error
# is = 10 #key word
# bad variable = 100 #space is used error

#4
# x,y=1,2
# print(x,y)
# x,y=y,x #swapping without a common container
# print(x,y)

#5
# if True: 
#   print('first')
# else:   #will never come to else because always the if condition is satisfied
#   print('second')

#6
# #Left
# x=True
# if x == True:
#   print('works')
# #Right
# x=True
# if x:
#   print('works')
# #Both x are accepting boolean values, Left has a redundant operation to check if the condition is satisfied

#7
# x=int(input()) #should get the input as an int or else it stores as string
# if x%10==0:
#   print('multiple of 10')
# elif (x%5==0) and (x%10!=0):
#   print('multiple of 5 and not a multiple of 10')
# else:
#   print('neither a multiple of 5 nor a multiple of 10')
# #if loop structure is if..elif..else order should be maintained

#8
# year = int(input())
# if year %4 ==0:
#   print('leap')
# else:
#   print('non-leap')
# #tries to show if the given input year is leap year or not, may fail for 2100, 1900,1800 years

#9
# x,y,z = int(input()),int(input()),int(input())
# if x==y and y==z:
#   print('equilateral')
# elif x==y and x!=z:
#   print('isosceles')
# elif (x==z and x!=y) or (y==z and y!=x): #even without bracket meaning doesn't change
#   print('isosceles')
# # elif y==z and y!=x:
# #   print('isosceles')
# else:
#   print('scalene')
# # Left out a condition for the isosceles triangle 
# #instead of so many elif for the same print could have added condition in single elif

#10
# userInput = int(input())
# isOdd = userInput % 2
# if isOdd:
#   print('odd')
# else:
#   print('even')

#11
# a=int(input())
# b=a%10

# if b == 0:
#   print('zero')
# elif b ==1:
#   print('one')
# elif b ==2:
#   print('two')
# elif b ==3:
#   print('three')
# elif b ==4:
#   print('four')
# elif b ==5:
#   print('five')
# elif b ==6:
#   print('six')
# elif b ==7:
#   print('seven')
# elif b ==8:
#   print('eight')
# else:
#   print('nine')

#12
# x,y,z= int(input()),int(input()),int(input())

# if x==y+z or y==x+z or z==x+y:
#   print('good triplet')
# else:
#   print('bad triplet')

#13
# x,y,z= float(input()),float(input()),float(input()) #Float to get all the real numbers
# if x>=0 and y>=0 and z >=0 : #to check non negative
#   if x!=0 and y!=0 and z!=0: # all 3 sides must be greater than 0 for a triangle
#     print('True')
#   else:
#     print('False')
# else:
#   print('Enter non-negative real numbers')

#14
# a,b,c,d=int(input()),int(input()),int(input()),int(input()) #integer as input
# if(a<b<c<d): #condition to check ascending order and distinct integers
#   print('in ascending order')
# else:
#   print('not in ascending order')

#15
# from calendar import *
# print(month(1994,6))
# #I was born on wednesday

#16
# alpha='abcdefghijklmnopqrstuvwxyz'
# shift=-5 #since it was encoded with +5, using -5 here
# inpString='udymts'
# outString=''
# outString=alpha[alpha.index(inpString[0])+shift]
# outString += alpha[alpha.index(inpString[1])+shift]
# outString += alpha[alpha.index(inpString[2])+shift]
# outString += alpha[alpha.index(inpString[3])+shift]
# outString += alpha[alpha.index(inpString[4])+shift]
# outString += alpha[alpha.index(inpString[5])+shift]
# print(outString)

#17
# #string
# empty='' #just a string, amy string will be considered as true except null string
# if empty:
#   print('if')
# else:
#   print('else')
# #number
# zero=0 #any number is considered to be true except 0
# if zero:
#   print('if')
# else:
#   print('else')

#18
# import math
# print(2**5)#will consider as int or float depending on input
# print(math.pow(2,5))#library function is used, will always consider as a float

#19
# print('before')
# print('\n')
# print('after')
# #two lines get printed before and after, this is because print statement by default takes cursor to next line after execution of print

#20
# a=int(input())
# b=a//100 #takes the 1st digit
# c=a%100//10 #takes the 2nd digit
# d=a%10 #takes the last digit
# print(a,b,c,d)
# if abs(b-d)==c: #abs() gives positive difference values, takes mod
#   print('sandwich')
# else:
#   print('plain')

#21
# message = 'Txt me when u receive this msg.'
# message=message.replace('Txt','Text')#will replace the Txt to text
# message=message.replace('u','you')
# message=message.replace('msg','message')
# print(message)

#22
#inpString = input()
#print(inpString.count(' ')+1)

#23
# inpString = input()
# print(inpString.count('.'))

#24
inpString=input()
outString=inpString.replace('O','0')
outNumber=int(outString)
print(outNumber)