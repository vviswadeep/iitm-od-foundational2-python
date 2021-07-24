# a=[]
# flag=True
# total=0
# while(flag):
#   b=input()
#   if(b=="END"):
#     flag=False
#   else:
#     a.append(b)
#     total+=int(b)
# print(a)
# print(total)
# avg=total/len(a)
# numeratorSum=0
# for i in a:
#   numeratorSum += (int(i)-avg)**2

# denominator = len(a)-1
# sigma = (numeratorSum/denominator)**0.5
# print(sigma)
# inputString=input()
# countBrac=0
# flag=False
# maxcount=0
# for i in inputString:
#   if i=="(":
#     countBrac+=1
#   elif i==")":
#     countBrac-=1
#   if countBrac<0:
#     flag=True
#     break
#   if countBrac>maxcount:
#     maxcount=countBrac
# if countBrac==0:
#   print(maxcount)
# elif flag:
#   print("Not matched")
# else:
#   print("Not matched")

# a=[]
# flag=True

# while(flag):
#   b=input()
#   if(b==""):
#     flag=False
#   else:
#     a.append(int(b))
# a.sort()
# for i in a:
#   flag2=True
#   for j in a:
#     if i+j in a:
#       if i!=j:
#         print(i,j)
#       if i==j and flag2 and a.count(j):
#         flag2=False
#         print(i,j)

# t={1}
# print(t)
# print(type(t))

# t=set()
# print(t)
# print(type(t))

# test = {1:{'name':"qwer"},2:{'mark':{'phy':80}}}
# print(test[2]['mark']['phy'])

# #test[3] = {'name':'asd'}
# test.update({3:{'name':'asd'}})
# del test[2]
# print(test)

malgudi = ['It', 'was', 'Monday', 'morning.', 'Swaminathan', 'was', 'reluctant', 'to', 'open', 'his','eyes.', 'He', 'considered', 'Monday', 'specially', 'unpleasant', 'in', 'the', 'calendar.', 'After', 'the', 'delicious', 'freedom', 'of', 'Saturday', 'And', 'Sunday,', 'it', 'was', 'difficult', 'to','get', 'into', 'the', 'Monday', 'mood', 'of', 'work', 'and', 'discipline.', 'He', 'shuddered', 'at','the', 'very', 'thought', 'of', 'school:', 'the', 'dismal', 'yellow', 'building;', 'the','fire-eyed', 'Vedanayagam,', 'his', 'class', 'teacher,', 'and', 'headmaster', 'with', 'his', 'thin', 'long', 'cane...']

# print(malgudi)

# P={}

# for i in range(1,len(malgudi)):
#   P[i]=[]

# for i in malgudi:
#   P[1] = ['test','wes']

# print(P)

# import http.client

# conn = http.client.HTTPSConnection("westus.api.cognitive.microsoft.com")
# payload = {"url":"https://upload.wikimedia.org/wikipedia/en/9/95/Test_image.jpg"}
# headers = {
#   'Content-Type': 'application/json',
#   'Ocp-Apim-Subscription-Key': 'fb847bc3a51848f394e4be2d7c91c07a'
# }
# conn.request("POST", "/vision/v3.2/ocr?language=unk&detectOrientation=true&model-version=latest", payload, headers)
# res = conn.getresponse()
# #data = res.read()
# #print(data.decode("utf-8"))
# print(res)

# import requests

# url = "https://westus.api.cognitive.microsoft.com/vision/v3.2/ocr?language=unk&detectOrientation=true&model-version=latest"

# payload="{\"url\":\"https://upload.wikimedia.org/wikipedia/en/9/95/Test_image.jpg\"}"
# headers = {
#   'Content-Type': 'application/json',
#   'Ocp-Apim-Subscription-Key': 'fb847bc3a51848f394e4be2d7c91c07a'
# }

# response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text)


def merge_sorted_list(l1,l2):
  l3=[]
  i,j=0,0
  while(i<len(l1)and j<len(l2)):
    if l1[len(l1)-i-1]<=l2[j]:
      l3.append(l1[len(l1)-i-1])
      i+=1
    else:
      l3.append(l2[j])
      j+=1
  return l3

l2=[1,2,4,9] #9
l1=[9,5,3] #9

print(merge_sorted_list(l1,l2))








l=[1,2,3,4,5,6,7,8,9]
i=0
s=0
while i<len(l):
  print("while",i)
  for i in range(i,l[i]):
    print(i,l[i])
    s+=l[i]
    i+=1
    print(s)
  i+=1




print(2 in l)
print(False == False)

print((1*2**5)+(0*2**4)+(0*2**3)+(1*2**2)+(0*2**1)+(0*2**0))



def BintoDec(n):
  print(n)
  if n==0:
    return 0
  else:
    return ((n)%10 + 2*BintoDec(n//10))

#print(BintoDec(101))
# 1+2*f(10)#1+2(2)=5
# 0+2*f(1) #0+2(1)
# 1+2*f(0) #1+0

# f(0)=0
n='Python'
for i in range(len(n)-1,-1,-1):
  print(i,n[i])
print("--------------------")
def b2d(n):
  decimal,i=0,0
  while(n!=0):
    dec=n%10
    print(dec, "dec")
    decimal = decimal + dec*pow(2,i)
    print(decimal,"decimal")
    n=n//10
    i=i+1
    print(n,i,"n,i")
  return decimal

print(b2d(101))


a=[1,3,1]
print(a==[1,1,3])

P=[1,2,3]
Q=[1,3,2]
def equality(P,Q):
  for elem in P:
    if elem not in Q:
      return False
  return True

print("---",equality(P,Q))

def equality(P,Q):
  if len(P) != len(Q):
    return False
  for elem in P:
    if elem not in Q:
      return False
  return True
print("---",equality(P,Q))


[1,2,3,4]
[1,2,3,4,5,6]

def is_pal(s):
  if len(s)==1:
    return True
  if s[0]==s[-1]:
    return is_pal(s[1:-1])
  else:
    return False

print(is_pal("madam"),"====")

inputlist=[1,2,3,4,5,7,8,9,6]


# def reverse(inputlist):
#     out=[]
#     while(len(inputlist)>0):
#         out.append(inputlist[-1])
#         print(out)
#         print(inputlist)
#         reverse(inputlist[:-1])
#     #return out

# print(reverse(inputlist))



def reverse(inputlist):
  out=[]
  print(inputlist)
  if len(inputlist)==1:
    out.append(inputlist[-1])
    print(out)
  else:
    print(out)
    reverse(inputlist[:-1])
  return out

print(reverse(inputlist))


# def max_element(inputlist):


db={
  "a":[1,2],
  "b":[2,3],
  "c":[6,7]
}

ad=('test:1',5,6)
def add(db,ad):
  db[ad[0]]=[ad[1],ad[2]]


print(db)

add(db,ad)
print(db)

def total_collection(db):
  sum=0
  for i in db.value():
    print(i)
    sum += i[0]
  return sum


