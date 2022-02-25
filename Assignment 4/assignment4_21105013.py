################ASSIGNMENT 4######################
print("ASSIGNMENT 4")
print("")
print("Question 1")
#Hanoi Tower with 3 discs
def hanoi(n,from_rod,to_rod,aux_rod):
    if n==1:
        print(f"Move disc 1 from rod {from_rod} to rod {to_rod} ")
        return
    hanoi(n-1,from_rod,aux_rod,to_rod)
    print(f"Move disc {n} from rod {from_rod} to rod {to_rod}")
    hanoi(n-1,aux_rod,to_rod,from_rod)

#calling function for n=3
hanoi(3,'A','B','C')

#######################################################
print("")
print("Question 2")
#Pascal's Triangle for n rows(taking input)
n=int(input("Please enter the number of rows required in the pascal triangle:"))

#Method 1 USING RECURSIONS
print("Using Recursions:\n")

def pascal(n,n_=n):
    if n==0:
        return

    pascal(n-1,n_)
    print(' '*(n_-n),end='')

    entry=1
    for i in range(1,n+1):
        print(entry,end=' ')
        entry=entry*(n-i)//i
    print()

pascal(n)

print()
#Method 2 USING ITERATIONS
print("Using Iterations:\n")
for line in range(1,n+1):
    print(' '*(n-line),end=' ')

    x=1
    for i in range(1,line+1):
        print(x,end=' ')
        x=x*(line-i)//i

    print()
print("")

#############################################################
print("Question 3")
#Taking input of two numbers
a=int(input("Please enter the first number:"))
b=int(input("Please enter the second number:"))
quotient=a//b
remainder=a%b
print("")
print("Part a")
if b!=0: 
    #defining a function
    def quorem(a,b):
        quotient=a//b
        remainder=a%b
        print ("The quotient is:",quotient)
        print ("The remainder is:",remainder)
        return quotient and remainder
    #calling function
    quorem(a,b)
else:
    print("The function is not callable.")
    
print("")
print("Part b")
#Check for non-zero
if a!=0 and b!=0:
    print("All the values are non-zero.")

print("")
print("Part c d")
set1=set()
for i in range (4,7):
    f=remainder+i
    g=quotient+i
    if (f>4):
        set1.add(f)
        print(set1)
    if (g>4):
        set1.add(g)
        print(set1)

print(set1)

print("")
print("Part e f")
#Frozen set
set2=frozenset(set1)
print("Immutable set:",set2)
print("")
#Maximum Value
h=max(set2)
print("The largest value in set is:",h)
print("")
#Hash Value
print("The hash Value:",hash(h))
print("")

######################################################################
print("Question 4")
#defining class
class Student:
    def __init__(self, student, sid):
        self.name = student
        self.sid = sid
    
    def __del__(self):
        print("Data Deleted")

#creating object
student1 = Student("Harsh Goyal", 21105013)
print("Data Recorded")

#printing the stored values
print(f"The name of the student is {student1.name} and SID is {student1.sid}.")

#destroying object
del student1
print("")

#######################################################################
print("Question 5")
#defining a class
class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def __del__(self):
        print(f"Employee {self.name} is deleted.")

#storing employees details
employee1 = employee("Mehak", 40000)
employee2 = employee("Ashok", 50000)
employee3 = employee("Viren", 60000)

print("Part a")
#updating details
employee1.salary = 70000
print(f"The updated salary of the employee {employee1.name} is Rs.{employee1.salary}")

print("Part b")
#deleting details
print("",end='')
del employee3

print(" ")

#########################################################################
print("Question 6")
#inputting a word from George
word = input("Enter the word: ")

#inputting a meaningful word with the exact same letters
word_ = input("\nEnter a new meaningful word using exact letters to test your friendship: ")

#defining dictionary
def count_in_dict(word):
    count = {}
    list1 = list(word)
    
    n = len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]] += 1
        else:
            count[list1[i]] = 1
    return count

#test to verify the letters of the new word
if count_in_dict(word) != count_in_dict(word_):
    print("The letters aren't exact, friendship is fake!!")


def userinput():
    ans = input("\nDoes the word makes sense?(y or n)\n")

    if ans == 'y':
        print("The friends pass the friendship test!!\n\n")
    elif ans == 'n':
        print("The word doesn't have a meaning, friendship is fake!!\n\n")
    else:
        print("Invalid input, try again")
        userinput()
userinput()
print("")

############################################################################
