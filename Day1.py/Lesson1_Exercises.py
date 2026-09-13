# Part A - Warm-up: Python basics
#1.Print your name, the course name and today's study goal on separate lines

print("my name is Gowtami Devarenti")
print("Course: Python fundamentals")
print("today's study goal : to learn python basics")



#2. Create variables for a person's name, age, height in meters and whether they are
# currently a student. Print both the values and their types.


name = "Gowtami Devarenti"
age = 33
height = 5.4
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

print("Type of Name:", type(name))
print("Type of Age:", type(age))
print("Type of Height:", type(height))
print("Type of Is Student:", type(is_student))


#3. Change the value stored in one variable to a different data type. Print its type before
#and after the change. Explain in a comment what this demonstrates about Python.

#i understood that Change the value stored in one variable to a different data type. Print its type before and after the change. 
#for example age = if we give number we can change to string and vice versa. python is dynamically typed language so we can change the data type of variable at any time.

age = 33
print("Type of Age before change:", type(age))

#now changing the value of age to a string
age = "33"
print("Type of Age after change:", type(age))

#same variable but different data type. 

#4. Create two numeric variables and calculate addition, subtraction, multiplication,
#normal division, floor division, remainder and exponentiation. Print a readable label
#before each result.

#Create two numeric variables

a=5
b=3
print("Addition of a and b:", a + b)
print("Subtraction of a and b:", a - b)
print("Multiplication of a and b:", a * b)
print("Normal Division of a and b:", a / b)
print("Floor Division of a and b:", a // b)
print("Remainder of a and b:", a % b)
print("Exponentiation of a and b:", a ** b)


#5. Write three examples where explicit type conversion is necessary: string to int, int to
#float and number to string.
#changing one data type into another data type is called explicit type conversion.



#String to int


number = "100"
print(number)
print(type(number))
number = int(number)
print(type(number))


#Int to float

a = 10
a = float(a)
print(a)
print(type(a))



#number to string

NUMBER = 200
print(NUMBER)
print(type(NUMBER))
NUMBER = str(NUMBER)
print(NUMBER)
print(type(NUMBER))

#Part B - User input and calculations

#Profile program
#name = input("Enter your name: ")
#year_of_birth = int(input("Enter your year of birth: "))

#current_year = 2026
#age = current_year - year_of_birth
#print(f"Hello {name}, you are approximately {age} years old.")

#Price and discount

#price = float(input("Enter the price: "))
#discount_percentage = float(input("Enter the discount percentage: "))

#discount_amount = price * discount_percentage / 100

#final_price = price - discount_amount

#print(f"Final price: {final_price:.2f}")
# .2f is used to format the final price to two decimal places for better readability.


#Celsius to Fahrenheit

celsius = float(input("Enter the temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print(f"Temperature in Fahrenheit: {fahrenheit:.2f}")

