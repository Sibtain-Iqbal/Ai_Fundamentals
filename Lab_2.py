inp1=int(input("enter a number"))
inp2=int (input("enter a number"))
inp3=int (input("enter a number"))

if(inp1<inp2 and inp1<inp3):
    print("minimum is",inp1)

elif(inp2<inp1 and inp2<inp3):
    print("minimum is",inp2)

elif(inp3<inp1 and inp3<inp2):
    print("minimum is",inp3)
else:
    print ("sorry")

    
if(inp1>inp2 and inp1>inp3):
          print("maximum is",inp1)
  
elif(inp2>inp1 and inp2>inp3):
    print("maximum is",inp2)

elif(inp3>inp1 and inp3>inp2):
    print("maximum is",inp3)
else:
    print("sorry")

    

x=7
print(x,"---",2*x,"---",3*x,"---",4*x,"---")



number_1=int(input("enter a nuber from 1 to 10"))
print("square is",number_1**2)
print("cube is",number_1**3)
             







a = 9 - 3
print(a)
b =	8 * 2.5
print(b)
c = 9 / 2
print(c)
d	=9 / -2
print(d)
e =	9 // -2
print(e)
f =	9 % 2
print(f)
g =	9.0 % 2
print(g)
h =	9 % 2.0
print(h)
i =	9 % -2
print(i)
j =	-9 % 2
print(j)
k =	9 / -2.0
print(k)
l =	4 + 3 * 5
print(l)
m =	(4 + 3) * 5
print(m)


p,q = 5,6
p = int(p*q)
q = int(p/q)
p = int(p/q)
print(p,q)



input_1 =int(input("enter number 1"))
input_2 = int (input("enter number 2"))
print("the sum is",input_1+input_2)
print ("the multiplication is",input_1*input_2)
print ("the division is ",input_1/input_2)
print("the modulus is",input_1%input_2)
print ("the difference is",input_1-input_2)


radius = int(input("enter a radius"))
print("the circumference is",2*3.14*radius)
print("the diameter is ",radius*2)
print("the area is",3.14*radius**2)


print("*********")
print("*       *")
print("*       *")
print("*       *")
print("*********")




print("   *** ")
print("*       *")
print("*       *")
print("*       *")
print("*       *")
print("   *** ")


print("  *  ")
print(" *** ")
print("*****")
print("  *  ")
print("  *  ")
print("  *  ")
print("  *  ")
print("  *  ")


print("   *   " )
print("  * * ")
print(" *   * ")
print("*     * ")
print(" *   *  ")
print("  * * ")
print("   *  ")






print("HHHHHH")
print(" HHHHH")
print("  HHHH")
print("   HHH")
print("     H")





number = int (input("enter a number"))
if(number%2==0):
    print("even")

else:
    print("odd")









num1=int(input("enter a number"))
num2=int(input("enter a number"))
num3=int(input("enter anumber"))
num4=int(input("enter a number"))
num5= int(input("enter a number"))
if num1<num2 and num1<num3 and num1<num4 and num1<num5:
    small=num1
if num2<num1 and num2<num3 and num2<num4 and num2<num5:
    small=num2
if num3<num1 and num3<num2  and num3<num4 and num3<num5:
    small=num3
if num4<num1 and num4<num2 and num4<num3 and num4<num5:
    small=num4
if num5<num1 and num5<num2 and num5<num3 and num1<num4:
    small=num5
if num1>num2 and num1>num3 and num1>num4 and num1>num5:
    large=num1
if num2>num1 and num2>num3 and num2>num4 and num2>num5:
    large=num2
if num3>num1 and num3>num2 and num3>num4 and num3>num5:
    large=num3
if num4>num1 and num4>num2 and num4>num3 and num4>num5:
    large=num4
if num5>num1 and num5>num2 and num5>num3 and num5>num4:
    large=num5
print("largest is",large)
print("smalllest is ", small)



num1=int(input("enter a number"))
num2= int(input("enter a number"))
num3= int(input("enter a number"))
if num1**2+num2**2==num3**2 or num2**2+num3**2==num1**2 or num1**2+num3**2==num2**2:
    print("three integers are side of right triangle")
else:
    print("three integers are not the side of right triangle")





marks=float (input ("Enter your score: "))
if 1>marks>=0.9:
    print("a")
elif 1>marks>=0.8:
    print("b")
elif 1>marks>=0.7:
    print("c")
elif 1>marks>=0.6:
    print("d")
elif 1>marks<0.6:
    print("f")
else:
    print("bad score")









#bonus
clock=int (input ("Enter hour: ")) 
m=input("am or pm? ")
ahead=int (input ("How many hours ahead? "))
a=clock+ahead
hour=(a)%24
if 0<hour<12:
    print (hour, m)
elif hour==0:
    if m=='am':
        print (12, 'pm' )   
elif m=='pm' :
    print (12, 'am')
elif hour>12 and clock!=12:
    if m=='am':
        print (hour-12, 'pm' ) 
elif m=='pm' :
    print (hour-12, 'am')
else:
    print (hour-12, m)