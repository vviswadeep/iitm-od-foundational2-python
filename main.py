# f=open('test.txt','r')
# nums=list()
# line=f.readline().strip()
# print(nums, line, type(f))
# while(line!=''):
#   nums.append(int(line))
#   line=f.readline().strip()

# f.close()
# print(line)

L = ['1','2','3','4','5']
for x in L:
  x=int(x)
  print(x,type(x))
print(L)

L='n\no\nn\ne'
for c in L:
  print(c,end='')

L=[5,6]
L=L[1:]
print(L)
L=L[:-1]
print(L)


print(1%0)
L=(1,2,3)
for a in L:
  print(a)