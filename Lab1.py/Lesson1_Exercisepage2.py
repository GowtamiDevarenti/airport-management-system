
# Part C – Strings

### 1.Store a full sentence in a variable. Print its length, uppercase version, lowercase version, and a version with leading/trailing whitespace removed.


sentence = "   Python is powerful and versatile.   "

print(len(sentence))
print(sentence.upper())
print(sentence.lower())
print(sentence.strip()) #strip() = remove whitespace from the start and end.


##2.Ask for first name and last name. Create a formatted full name using an f-string.

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

full_name = f"{first_name} {last_name}" #The f tells Python that you want to insert variables inside {}.

print(full_name)


# 3.Given the string 'python programming', print the first character, last character,
# first six characters, last eleven characters, and the entire string reversed.



text = "python programming"

print(text[0])       # First character
print(text[-1])      # Last character
print(text[:6])      # First six characters
print(text[-11:])    # Last eleven characters
print(text[::-1])    # Reverse the entire string


### 4.Create a username generator: ask for first and last name, remove surrounding spaces,
#convert to lowercase, and create a username using the first three letters of the first name 
# plus the first five letters of the last name.

first_name = input("Enter your first name: ").strip().lower()
last_name = input("Enter your last name: ").strip().lower()

username = first_name[:3] + last_name[:5]
print("Generated username:", username)

### 5.Given an email address, use string operations to extract the part before @ and the domain 
#after @. Assume exactly one @ for this exercise.

email = input("Enter your email address: ")
local_part, domain = email.split('@')

print("Local part:", local_part)
print("Domain:", domain)



### 6.Create a sentence containing the word 'Java'. 
# Replace it with 'Python' and print both the original and changed sentence.

sentence = "I like to code in Java."
new_sentence = sentence.replace("Java", "Python")

print("Original sentence:", sentence)
print("Changed sentence:", new_sentence)

# Part D – String Investigation

### 1.Predict the output of at least eight expressions using indexing and
#slicing before running them. Include positive indexes, negative indexes, omitted start/end values, and a step.

Name = "Gowtami Devarenti"

# Positive indexing
print(Name[0])       # Prediction: G
print(Name[3])       # Prediction: t

# Negative indexing
print(Name[-1])      # Prediction: i
print(Name[-3])      # Prediction: t

# Slicing with start and end
print(Name[0:7])     # Prediction: Gowtami
print(Name[8:17])    # Prediction: Devarenti

# Omitted start value
print(Name[:7])      # Prediction: Gowtami

# Omitted end value
print(Name[8:17])    # Prediction: Devarenti

# Step
print(Name[::2])     # Prediction: Gwtm eaet
print(Name[::-1])    # Prediction: itneraveD imatwoG


### 2.Create a variable containing 'Artificial Intelligence'.
#Produce at least six different slices from it and comment what each slice means.



text = "Artificial Intelligence"

# 1. Get the first 10 characters
print(text[:10])       # Artificial


# 2. Get the word "Intelligence"
print(text[11:])      # Intelligence

# 3. Get characters from index 0 to 8
print(text[0:9])       # Artificia

# 4. Get the first 5 characters
print(text[:5])       # Artif

# 5. Get the last 5 characters
print(text[-5:])      # gence


# 6. Get every second character
print(text[::2])      # Atfcai itliec


#### 3.Investigate the difference between .split(), .strip(), .
#replace() and the in operator. Write one useful example of each.

# 1. split()
# split() breaks a string into a list of smaller parts.
sentence = "Python is easy"
words = sentence.split()

print(words)
# Output: ['Python', 'is', 'easy']


# 2. strip()
# strip() removes whitespace from the beginning and end of a string.
name = "   Gowtami   "
clean_name = name.strip()

print(clean_name)
# Output: Gowtami


# 3. replace()
# replace() changes one part of a string into another.
text = "I like Java"
new_text = text.replace("Java", "Python")

print(new_text)
# Output: I like Python


# 4. in operator
# The 'in' operator checks whether something exists inside a string.
email = "gowtami@gmail.com"

print("@" in email)
# Output: True


### 4.Demonstrate string immutability: attempt conceptually to change one character, 
###explain why direct character assignment fails, then create a new modified string instead.

name = "Amarnathreddy"

# Strings are immutable, so we cannot change one character directly.
# This would give an error:
# name[0] = "B"

# Instead, create a new modified string.
new_name = "Bhumireddy Amarnath Reddy"

print(new_name)


#Part E – Applied Challenge: Registration Summary
### 1.Build a console program that collects:
# first name, last name, city, year of birth, and favourite programming language.
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
city = input("Enter your city: ")
year_of_birth = int(input("Enter your year of birth: "))
fav_language = input("Enter your favourite programming language: ")


### 2.Normalize text input so accidental surrounding spaces do not affect the result.
# .strip() removes accidental leading and trailing whitespace
# .strip() removes accidental leading and trailing whitespace
first_name = input("Enter your first name: ").strip()
last_name = input("Enter your last name: ").strip()
city = input("Enter your city: ").strip()
year_of_birth = int(input("Enter your year of birth: ").strip())
fav_language = input("Enter your favourite programming language: ").strip()
### 3.Create a generated user ID from parts of the person's name and year of birth.
# Formula: First 3 letters of last name + first initial + last 2 digits of birth year
user_id = (last_name[:3] + first_name[:1] + str(year_of_birth)[-2:]).lower()

print(f"Generated User ID: {user_id}")
# Example: "John Doe" born in 2002 -> "doej02"

### 4.Print a clean multi-line summary using f-strings.
summary = f"""
========================================
         REGISTRATION SUMMARY
========================================
Full Name          : {first_name.title()} {last_name.title()}
User ID            : {user_id}
City               : {city.title()}
Year of Birth      : {year_of_birth}
Favourite Language : {fav_language.capitalize()}
========================================
"""
print(summary)

### 5.Print the initials, full name length excluding the space, and the favourite language reversed.

# Initials
initials = f"{first_name[0].upper()}.{last_name[0].upper()}."

# Full name length excluding space
name_length_no_space = len(first_name) + len(last_name)

# Reversed language using step slicing [::-1]
reversed_language = fav_language[::-1]

print(f"Initials              : {initials}")
print(f"Name Length (no space): {name_length_no_space} characters")
print(f"Reversed Language     : {reversed_language}")

### 6.Add at least three extra pieces of derived information of your own choice using only concepts from Lesson 1.

# Derived 1: Approximate age based on current year (2026)
approx_age = 2026 - year_of_birth

# Derived 2: Suggested corporate/school email address
suggested_email = f"{first_name.lower()}.{last_name.lower()}@techacademy.edu"

# Derived 3: Airport-style 3-letter city code in uppercase
city_code = city[:3].upper()

print(f"Approximate Age : {approx_age} years old")
print(f"Suggested Email : {suggested_email}")
print(f"City Code       : {city_code}")

# Part F – Stretch Challenges: Python Foundation

### 1.Create a simple seconds converter: input total seconds and calculate whole hours, remaining minutes, and remaining seconds using // and %.

total_seconds = int(input("Enter total seconds: "))

# 3600 seconds in 1 hour
hours = total_seconds // 3600
remaining_after_hours = total_seconds % 3600

# 60 seconds in 1 minute
minutes = remaining_after_hours // 60
seconds = remaining_after_hours % 60

print(f"{total_seconds} seconds = {hours} hour(s), {minutes} minute(s), and {seconds} second(s).")

### 2.Given a four-digit integer, extract and print each digit without converting the number to a string.
num = int(input("Enter a 4-digit integer: "))  # e.g., 5824

# Extract each digit using integer division (//) and modulo (%)
digit_thousands = num // 1000            # 5824 // 1000 = 5
digit_hundreds  = (num // 100) % 10      # 5824 // 100 = 58  -> 58 % 10 = 8
digit_tens      = (num // 10) % 10       # 5824 // 10 = 582  -> 582 % 10 = 2
digit_units     = num % 10               # 5824 % 10 = 4

print("Extracted digits:")
print(f"Thousands : {digit_thousands}")
print(f"Hundreds  : {digit_hundreds}")
print(f"Tens      : {digit_tens}")
print(f"Units     : {digit_units}")

### 3.Create a text masking program that displays only the first two and last two characters of a supplied word, replacing the middle with * characters.

word = input("Enter a word: ").strip()

if len(word) <= 4:
    # Too short to hide middle characters
    masked_word = word
else:
    # First 2 + asterisks for the middle length + last 2
    middle_mask = "*" * (len(word) - 4)
    masked_word = word[:2] + middle_mask + word[-2:]

print(f"Masked Word: {masked_word}")
# Example: "PASSWORD" -> "PA****RD"

### 4.Write five short *"predict before running"* examples that you could give to another student. Include at least one type conversion and two string slices.

#Example 1 (Type Conversion & Concatenation)
val = "12"
print(int(val) + int(val + "3"))
#Prediction: 135
#Why: val + "3" produces the string "123". int("12") + int("123") evaluates to 12 + 123 = 135.

#Example 2 (String Slicing with Step)

alphabet = "abcdefghijkl"
print(alphabet[1:9:3])
#Prediction: 'beh'
#Why: Starts at index 1 ('b'), stops before index 9 ('j'), taking every 3rd character: indices 1 ('b'), 4 ('e'), and 7 ('h').

#Example 3 (Reverse String Slicing)

message = "Developer"
print(message[-3::-2])
#Prediction: 'pedv'
#Why: Starts at index -3 ('p'), steps backward by 2: 'p', 'e', 'd', 'v'.

#Example 4 (Division and Modulo Precedence)
result = 17 // 3 + 17 % 3 * 5
print(result)
#Prediction: 15
#Why:
#17 // 3 = 5
#17 % 3 = 2
#Multiplication comes before addition: 2 * 5 = 10
#5 + 10 = 15.


#Example 5 (Slice and Type Conversion Combined)

code = "987654"
num = int(code[:3]) - int(code[-2:])
print(num)
#Prediction: 933
#Why: code[:3] is "987" (int: 987), and code[-2:] is "54" (int: 54). 987 - 54 = 933.

