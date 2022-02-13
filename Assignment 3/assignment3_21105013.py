#########ASSIGNMENT 3###########


print("Question 1")
#taking input from user
string = input("Please give an input- ")
string=string.lower().strip()
i=0
#defining empty dictionary 
dict={}

if " " not in string:
     #searching for common elements
     while i<len(string):
          counter=0
          k=0
          while k<len(string):
               if string[i]==string[k]:
                    counter=counter+1
                    k=k+1
               else:
                    k=k+1
          #storing the values in dictionary
          dict[f"{string[i]}"]=counter
          i=i+1

else:
     list = str.split(string)
     #searching for common words
     while i<len(list):
          counter=0
          k=0
          while k<len(list):
               if list[i]==list[k]:
                    counter=counter+1
                    k=k+1
               else:
                    k=k+1
                    #storing the pairs in dictionary
          dict[f"{list[i]}"]=counter
          i=i+1
#Printing the final result
print("Total occurances")
for key,value in dict.items():
    print(f"{key}-{value}")

    

print("Question 2")
#Taking input from user
day=int(input('Please enter Day- '))
month=int(input('Please enter Month- '))
year=int(input('Please enter Year- '))


if day>30 and month in {2,4,6,9,11}:
    condition=False
elif day>31 and month in {1,3,5,7,8,10,12}:
    condition=False
elif (day==29 or day==30) and month==2 and year%4!=0:
    condition=False
elif day==30 and month==2 and year%4==0:
    condition=False
else:
    condition=True


if condition:
    #months with 30 days
    if day==31 and month==12:
        next_year=year+1
    else:
        next_year=year
    if month==12 and day==31:
        next_month=1
    else:
        next_month=month
 #months with 31 days
    if month in {1,3,5,7,8,10,12}:
        if day==31:
            next_day=1
            if month!=12:
                next_month=month+1
            else:
                next_month=1
        else:
            next_day=day+1
    #month of february
    elif month==2:
        if year%4==0:
            if day==29:
                next_day=1
                next_month=3
            else:
                next_day=day+1
        else:
            if day==28:
                next_day=1
                next_month=3
            else:
                next_day=day+1
                    
    #remaining cases
    else:
        if day==30:
            next_day=1
            next_month=month+1
        else:
            next_day=day+1
    
    print(f"Next Date is: {next_day}/{next_month}/{next_year}")
else:
    print("That's not a valid date")


print("Question 3")
#given list
list=[3,5,7,8,9,11]
print(list)

#defining an empty list to store tuple pairs later
list_=[]
for i in list:
    tuple=(i,i**2)
    list_.append(tuple)
print(list_)


print("Question 4")
#getting input of grades from user
grades=int(input("Please input grade points between 4 and 10:\n"))
if (grades>=4 and grades<=10):
    if grades==4:
        performance="Poor"
        letter_grade="D"
    elif grades==5:
        performance="Below Average"
        letter_grade="C"
    elif grades==6:
        performance="Average"
        letter_grade="C+"
    elif grades==7:
        performance="Good"
        letter_grade="B"
    elif grades==8:
        performance="Very Good"
        letter_grade="B+"
    elif grades==9:
        performance="Excellent"
        letter_grade="A"
    else:
        performance="Outstanding"
        letter_grade="A+"
else:
    print("ERROR!! Check your input grade..")
#printing the final results
print(f"Your Grade is '{letter_grade}' and {performance} Performance")


print("Question 5")
#defining the list of all the alphabets
alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']

for row in range(0,6):
    column=0
    counter=0
    while column<11:
        if column<row or column>11-row-1:
            print(" ", end="")

        else:
            print(alphabets[counter], end="")
            counter=counter+1
        column=column+1
    print("")


print("Question 6")

condition=True
Dictionary={} # empty dictionary
prompt="y"
while condition:
    if prompt.lower()=="y":
                  #getting input of students details 
        SID=int(input("Please Enter SID of Student- "))
        name=input("Please enter the name of the Student- ")
        Dictionary[SID]=name
        prompt= input("If you want to enter more details press Y/N- ")
        condition = True

    else:
        condition = False

print("Part a")
for key,value in Dictionary.items():
    print(f"{key} is {value}")
print("")

print("Part b")
Val_sort_dict= sorted(Dictionary.values())
print(f"value sorted dictionary is {Val_sort_dict}")
print("")

print("Part c")
Key_sort_dict= sorted(Dictionary.keys())
print(f"Keys sorted dictionary is {Key_sort_dict}")
print("")

print("Part D")
SID_tbf=int(input("Please enter the student's SID whose detail you need- "))
if SID_tbf in Dictionary.keys():
    print(f"Name of the required student is {Dictionary[SID_tbf]}")
else:
    print("The SID is not present in the given Data")
print("")


print("Question 7")
number=int(input("Total required terms of Fibonacci sequence:"))
a1=1
a2=0
n=0
sum=a1+a2
print(f"Fibonnaci sequence with {number} terms")
print(a2)
print(a1)
#defining fibonacci sequence
while n<number-2:
    a=a2+a1
    a2=a1
    a1=a
    print(a)
    n=n+1
    sum+=a
average=sum/number
#printing final average of required fibonacci sequence 
print(f"Average of total {number} terms of sequence is {average}")
print("END")


print("Question 8")
#defining the given sets
Set1= {1, 2, 3, 4, 5}
Set2= {2, 4, 6, 8}
Set3= {1, 5, 9, 13, 17}

print("Part a")
set_notboth=Set1^Set2
print(f"set with elements not common in both is {set_notboth}")

print("Part b")
set_onlyinone=Set1^Set2^Set3
print(f"Set of elements that is only present in one set is {set_onlyinone}")

print("Part C")
set_onlyintwo=(Set1|Set2|Set3)- (Set1^Set2^Set3)-(Set1&Set2&Set3)
print(f"Set of elements that is only present in two set is {set_onlyintwo}")

print("Part d")
new_set1=set()
for n in range(1,11):
    new_set1.add(n)
not_common_1=new_set1- Set1
print(f"set of all integers in the range 1 to 10 that are not in Set1 {not_common_1}")

print("Part e")
new_set2=set()
for n in range(1,11):
    new_set2.add(n)
not_common_2=new_set2 - (Set1|Set2|Set3)
print(f"set of all integers in the range 1 to 10 that are not in Set1 and Set2 and Set3 {not_common_2}")
