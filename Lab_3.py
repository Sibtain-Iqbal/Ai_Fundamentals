thislist =("apple","banana","cherry")
print(thislist)
print(thislist[2])
print(thislist[1])
print(thislist[0])
print(thislist[-2])
print(thislist[-1])
print(thislist[-3])







list = ["cherry","apple","mango"]
list.insert(1,"orange")
list

list = ["cherry","apple","mango"]
list.append("orange")
list



tuple = ["cherry","apple","mango"]
tuple[-2]



set={"apple","banana","kiwi"}
for x in set:
    print(x)



set={"apple","banana","kiwi"}
set.remove("banana")
print(set)



dict = { "name":"iqra","class":"bsit"}
dict.pop("class")
print(dict)



##task 1
num1=int(input("enter a number"))
num2=int(input("enter a number"))
num3=int(input("enter a number"))
num4=int(input("enter a number"))
print("the sum is :",num1+num2+num4)
if (num1<num2<num3<num4):
    small = num1
    print("smallest is:",num1)
elif(num2<num1<num3<num4):
    small = num2
    print("smallest is:",num2)
elif(num3<num4<num2<num1):
    small = num3
    print("smallest is",num3)
elif(num4<num1<num2<num3):
    small = num4
    print("smallest is",num4)



#task 2
n = 5
i=1
factorial = 1
print("x factorial of x")
if n>=1:
    for i in range(1,n+1):
        factorial = factorial*i
        print(i,"factorial is:",factorial)
        i+=1



#task3
rand=8
guess=11
print ('I chosen a number between 1 and 10. Try to guess it.')
while guess!=rand:
    guess=int (input ('Guess: '))
if guess==rand:
    print ("That's right! You guessed it")
else:
    print ("That is incorrect. Guess again.")






#task4
num1 = int(input("enter a integer:"))
num2 = int(input("enter a integer:"))
if num1<num2:
    small, large=num1, num2 
elif num1>num2:
    small, large=num2, num1
while small!=0:
    r=large%small
    large, small=small, r
    print ('The GCD of given number' ,num1, 'and',num2, 'is',large)





#task 5
n=int (input ('Enter the number: '))
i=2
prime=True
while i<n:
    if n%i==0:
        prime = False
        break
        i+=1
if prime:
    print(n,"is prime")
else:
    print(n,"is not prime")





#task5 (b)
n=1
num=1
pr='All prime numbers between 1 and 10000 are\n'
while(num<10000):
    num+=1
    prime=True
    i=2
    while i<num:
        if num%i==0:
            prime=False
            break
        i+=1
    if prime:
           pr=pr+str(num)+ '  '
print(pr)


#task 6
n = 1000
print("all armstrong number having four digit are:")
while n<10000:
    p1=n%10
    p2=(n%100)//10
    p3=(n%1000)//100
    p4=n//1000
    if p1**4+p2**4+p3**4+p4**4==n:
        print(n)
    n+=1
    








#task 7
for i in  range(1,101):
    print(i,"Sibtaii ALI")

#task 8
for i in range(1,21):
    print(i,'___',i**2)


#task 9
for i in range(8,90,3):
    print(i,end=',')



#task 10
name = input("enter your name")
n = int(input("enter how many times you want to enter"))
for i in range(n):
    print(name)



#task 11
w=int(input("enter width"))
h=int(input("enter height"))
for i in range(h):
    print("*"*w)



#task 12
height = int(input("enter a number"))
for i in range(h):
    print("*"*(i+1))




#task 13
height= int(input('enter height (must be odd):'))
n=height//2+1
for i in range(n):
    print(' '*(n-i-1),end=' ')
    print('*'*(2*i+1))
for j in range(n):
    print(' '*(j+1),end=' ')
    print('*'*(2*(i-j)-1))




#task 14
height= int(input("enter height"))
n=height+1
for i in range(1,n):
    space = i-2
    if space>0 and i!=n//2+1:
        print(' '*(n-i),end=' ')
        print('*',' '*(2*space+1),'*',sep=' ')
    elif space==0 and i!=n//2+1:
        print(' '*(n-i),end=' ')
        print('*',' ','*',sep=' ')
    elif i==n//2+1:
        print(' '*(n-i),end=' ')
        print('*'*(2*i-1))
    else:
        print(' '*(n-i),end=' ')
        print('*')