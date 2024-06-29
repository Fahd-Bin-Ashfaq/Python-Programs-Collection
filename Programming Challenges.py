#01
umbers = input("Enter three numbers separated by space: ")
a, b, c = map(int, numbers.split())  
if (a > b and a < c) or (a > c and a < b):
    median = a
elif (b > a and b < c) or (b > c and b < a):
    median = b
else:
    median = c
print("The median of the three numbers is: ", median)

#02
Sentance=input("Enter Sentance: ")
word=Sentance.split()
count=len(word)
print(count)

#03
num=int(input("enter number: "))
sum=0
for i in range(num):
    sum=sum+i
print(sum)    

#04
strs = ["flower", "flow", "flight"]
prefix = strs[0] if strs else ""

for s in strs[1:]:
    
    while not s.startswith(prefix):
        prefix = prefix[:-1]
        if prefix == "":
            break
print("Longest common prefix:", prefix)

#05
num=int(input("enter number: "))
if num==1:
  print(num,"is prime number:") 
if num==0:
    print("Enter positive number: ")    
     
elif(num//num==1  ):
    print(num," is prime number")

    
    
  