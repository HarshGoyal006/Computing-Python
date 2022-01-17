print("Assignment 2")


print("Progr. 1a")
string="Python is a case sensitive language"
length=len(string)
print("The length of input string is:",length)

print("Prog. 1b")
string="Python is a case sensitive language"
gnirts=string[::-1]
print("The reversed string is\n",gnirts)

print("Prog. 1c")
remark="Python is "
remark_=remark+'a case sensitive'
print(remark_)

print("Prog. 1d")
remark_="Python is a case sensitive"
remark__=remark_.replace('a case sensitive','object oriented')
print(remark__)

print("Prog. 1e")
string="Python is a case sensitive language"
str=string.find('a')
print("The index of a is:\n",str)

print("Prog. 1f")
string="Python is a case sensitive language"
string_=string.replace(' ','')
print("The string without spaces is:\n",string_)

print("Prog. 2")
name=" Harsh Goyal "
SID=" 21105013 "
department=" ECE "
CGPA=" 8.1 "
output='Hey,'+ name + 'Here!\n' +'My SID is' + SID + '\nI am from '+ department + 'and my CGPA is' + CGPA
print(output)

print("Prog. 3")
a=56
b=10
print("a \nThe value of a AND b is:\n",a%b)
print("b \nThe value of a OR b is:\n",a|b)
print("c \nThe value of a XOR b is:\n",a^b)
print("d \nThe value of a after left shift with 2 bits is:\n",a<<2)
print("The value of b after left shift with 2 bits is:\n",b<<2)
print("e \nThe value of a after right shift with 2 bits is:\n",a>>2)
print("The value of b after right shift with 4 bits is:\n",b>>4)

print("Prog. 4")
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
num3=int(input("enter third number:"))
if num1>num2 and num1>num3:
 print("The greatest of three numbers is : num1")
elif num2>num1 and num2>num3:
 print("The greatest of three numbers is : num2")
else: 
 print("The greatest of three numbers is : num3")

print("Prog. 5")
string=input("Write your string here:")
print(string)
if "name" in string:
 print("Yes")
else:
 print("No")

print("Prog. 6")
a_=input("side 1 of triangle:")
b_=input("side 2 of triangle:")
c_=input("side 3 of triangle:")
a=int(a_)
b=int(b_)
c=int(c_)
if a<b+c and b<a+c and c<a+b:
 print("Yes")
else:
 print ("No")

















