print("Assignment 1")


print("Progr. 1")
num1=int(input("enter number 1 :"))
num2=int(input("enter number 2 :"))
num3=int(input("enter number 3 :"))
avg=(num1+num2+num3)/3
print("The average of given numbers is :",avg)


print("Progr. 2")
Tax_Rate=0.20
Standard_Deduction=10000
Dependent_Deduction=3000
Dependents_Number=int(input("Number of Dependents :"))
Gross_Income=float(input("The Gross Income is:"))
Taxable_Income=Gross_Income-Standard_Deduction-(Dependent_Deduction*Dependents_Number)
Tax=Taxable_Income*Tax_Rate
print("The Income Tax is :",Tax)


print("Progr. 3")
#Student_Record=[SID, Name, Gender, Department Name, CGPA]
Student=[21105013,'Harsh','M','ECE',8.4]
print(Student)


print("Progr. 4")
Marks=[87,23,45,27,98,60]
print("Marks without Sort",Marks)
Marks.sort
print("Marks with Sort",Marks)


print("Progr. 5a")
Colours=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Colours.pop(3)
print(Colours)


print("Progr. 5b")
Colours=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Colours[3:5]=['Purple']
print(Colours)