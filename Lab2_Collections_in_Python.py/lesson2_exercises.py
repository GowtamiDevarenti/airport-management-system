## Part A – Lists

#Create a list of at least eight programming languages. 
#Access the first, last, third and second-to-last values.


languages = [
    "Python",
    "Java",
    "C++",
    "JavaScript",
    "C",
    "C#",
    "Ruby",
    "Swift"
]

print("First:", languages[0])
print("Last:", languages[-1])
print("Third:", languages[2])
print("Second-to-last:", languages[-2])


#2. Print three different slices of the list, 
# then print the list in reverse order using slicing.

languages = [
    "Python",
    "Java",
    "C++",
    "JavaScript",
    "C",
    "C#",
    "Ruby",
    "Swift"
]

print(languages[0:3])
print(languages[2:6])
print(languages[4:8])

print("Reverse:", languages[::-1])


#3.Use append, insert, remove and pop. 
# After each operation, print the list so the change is visible.

fruits = ["Apple", "Banana", "Orange"]

# append
fruits.append("Mango")
print("After append:", fruits)

# insert
fruits.insert(1, "Grapes")
print("After insert:", fruits)

# remove
fruits.remove("Banana")
print("After remove:", fruits)

# pop
fruits.pop()
print("After pop:", fruits)


#4.Create a numeric list. Calculate its length, minimum, maximum and 
# sum using built-in functions.

numbers = [10, 20, 5, 40, 15, 30]

print("Length:", len(numbers))
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
print("Sum:", sum(numbers))

#5.Sort one list ascending and another descending. Explain in a comment the difference between changing a list with .
#sort() and creating a sorted result with sorted().

numbers1 = [5, 2, 8, 1, 9]

numbers1.sort()

print("Ascending:", numbers1)


numbers2 = [5, 2, 8, 1, 9]

numbers2.sort(reverse=True)

print("Descending:", numbers2)


numbers = [5, 2, 8, 1]

new_numbers = sorted(numbers)

print("Original:", numbers)
print("Sorted:", new_numbers)



#6. Demonstrate the reference/copy issue using list_b = list_a. 
# Then fix it with .copy().
list_a = ["Apple", "Banana", "Orange"]

list_b = list_a

list_b.append("Mango")

print("list_a:", list_a)
print("list_b:", list_b)



#Part B – Tuples and Unpacking


##Create a tuple representing RGB values. 
# Unpack it into three variables and print them.



rgb_values = (255, 128, 0)
red, green, blue = rgb_values

print("Red:", red)
print("Green:", green)
print("Blue:", blue)


##Create a tuple containing a person's name, age and city. 
# Unpack and use the values in a formatted sentence.



person = ("Alice", 30, "New York")
name, age, city = person

print(f"{name} is {age} years old and lives in {city}.")



##Attempt to reason about changing one tuple element. 
# Explain in a comment why tuples are useful when values should not be changed.

# Tuples are immutable, meaning their elements cannot be changed after they are created. 
# This makes them useful for storing data that should remain constant, such as configuration settings or fixed values.


##Create a list containing at least four coordinate tuples such as (10, 20). 
# Access individual x and y values.


coordinates = [(10, 20), (30, 40), (50, 60), (70, 80)]

for coord in coordinates:
    x, y = coord
    print(f"x: {x}, y: {y}")
    
    
    ## Part C – Sets

##1. Create a list containing duplicate course names. 
#Convert it to a set and compare the lengths before and after.

courses = ["Math", "Science", "History", "Math", "English", "Science"]

print("Before conversion:", len(courses))

courses_set = set(courses)
print("After conversion:", len(courses_set))


##Create two sets representing skills of two developers. 
#Find skills they share, skills only the first has, and all skills represented by either person.


developer1_skills = {"Python", "Java", "C++", "JavaScript"}
developer2_skills = {"Python", "JavaScript", "SQL", "React"}

shared_skills = developer1_skills & developer2_skills
developer1_unique_skills = developer1_skills - developer2_skills
all_skills = developer1_skills | developer2_skills

print("Shared skills:", shared_skills)
print("Developer 1's unique skills:", developer1_unique_skills)
print("All skills:", all_skills)


#Create a set and practice add, remove/discard and membership testing.

my_set = {"apple", "banana", "orange"}

my_set.add("grape")
print("After adding 'grape':", my_set)

my_set.remove("banana")
print("After removing 'banana':", my_set)

my_set.discard("orange")
print("After discarding 'orange':", my_set)

print("Is 'apple' in the set?", "apple" in my_set)


#Explain in comments 
# why a set is a better choice than a list for one real-world uniqueness problem.
# A set is a better choice than a list for representing unique elements because it automatically ensures that all elements are distinct. 
# This is useful in scenarios where you need to maintain a collection of unique items, such as storing a list of unique user IDs or distinct product codes.


## Part D – Dictionaries

#1. Create a dictionary for a laptop with brand, model, RAM, storage and price.
# Read every value by key.

laptop = {
    "brand": "Dell",
    "model": "XPS 13",
    "RAM": "16 GB",
    "storage": "512 GB SSD",
    "price": 1999.99
}

print("Brand:", laptop["brand"])
print("Model:", laptop["model"])
print("RAM:", laptop["RAM"])
print("Storage:", laptop["storage"])
print("Price:", laptop["price"])


#Update the price, add an operating_system key and remove one key.

laptop["price"] = 1899.99
laptop["operating_system"] = "Windows 10"
del laptop["storage"]
print("Updated laptop details:", laptop)

#Use .get() for both an existing and a missing key.
# Compare it conceptually with direct indexing.


print("Brand (using .get()):", laptop.get("brand"))
print("Non-existent key (using .get()):", laptop.get("non_existent_key", "Key not found"))

# indexing would raise a KeyError if the key does not exist, while .get() allows
# you to provide a default value and avoids an error.


#Print keys, values and items separately.

print("Keys:", list(laptop.keys()))
print("Values:", list(laptop.values()))
print("Items:", list(laptop.items()))

#Create a dictionary mapping five course names to number of study hours. 
#Calculate the total hours using the dictionary values.


study_hours = {
    "Math": 10,
    "Science": 8,
    "History": 6,
    "English": 5,
    "Art": 4
}

total_hours = sum(study_hours.values())
print("Total study hours:", total_hours)


## Part E – Nested collections
# -------------------------------------------------------------
# 1. Create a list of at least five dictionaries representing books
# -------------------------------------------------------------
books = [
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "pages": 281, "available": True},
    {"title": "1984", "author": "George Orwell", "pages": 328, "available": False},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "pages": 432, "available": True},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "pages": 180, "available": True},
    {"title": "Lord of the Flies", "author": "William Golding", "pages": 224, "available": False}
]

# -------------------------------------------------------------
# 2. Access the title of the third book and availability of the last book
# -------------------------------------------------------------
third_book_title = books[2]["title"]         # Index 2 is the 3rd book
last_book_availability = books[-1]["available"] # Index -1 is the last book

print("Third book title:", third_book_title)
print("Last book availability:", last_book_availability)

# -------------------------------------------------------------
# 3. Change one nested value and add a new key to one book
# -------------------------------------------------------------
# Change availability of the second book (index 1) to True
books[1]["available"] = True

# Add a new key 'genre' to the first book (index 0)
books[0]["genre"] = "Classic Literature"

print("\nUpdated Book 2:", books[1])
print("Updated Book 1 (with new key):", books[0])

# -------------------------------------------------------------
# 4. Dictionary where each key is a department and value is employee list
# -------------------------------------------------------------
company_departments = {
    "Engineering": ["Alice Chen", "Bob Miller", "Carlos Ruiz"],
    "Marketing": ["Diana Prince", "Edward Norton"],
    "Finance": ["Fiona Gallagher", "George Clark", "Hannah Abbott"]
}

print("\nEngineering team:", company_departments["Engineering"])

# -------------------------------------------------------------
# 5. Course structure for three courses and chained indexing
# -------------------------------------------------------------
courses = [
    {
        "name": "Introduction to Python",
        "teacher": "Dr. Angela Yu",
        "topics": ["Variables", "Control Flow", "Functions", "Data Structures"]
    },
    {
        "name": "Web Development",
        "teacher": "Colt Steele",
        "topics": ["HTML5", "CSS3", "JavaScript", "React"]
    },
    {
        "name": "Database Systems",
        "teacher": "Prof. Jennifer Widom",
        "topics": ["Relational Model", "SQL Queries", "Indexing", "Transactions"]
    }
]

# Chained indexing: course at index 0 -> key 'topics' -> topic at index 2
selected_topic = courses[0]["topics"][2]
print("\nSelected topic from Course 1:", selected_topic)  # Output: Functions




#Part F – Applied Challenge: Personal Media Catalogue
# -------------------------------------------------------------------------
# 1 & 2 & 4. Catalogue stored as a list of dictionaries with 4+ useful fields,
#            including an immutable tuple (identifier, release_year).
# -------------------------------------------------------------------------
catalogue = [
    {
        "id_info": ("MOV-101", 2010),
        "title": "Inception",
        "genre": "Sci-Fi",
        "rating": 8.8,
        "director": "Christopher Nolan"
    },
    {
        "id_info": ("MOV-102", 1999),
        "title": "The Matrix",
        "genre": "Sci-Fi",
        "rating": 8.7,
        "director": "The Wachowskis"
    },
    {
        "id_info": ("MOV-103", 2008),
        "title": "The Dark Knight",
        "genre": "Action",
        "rating": 9.0,
        "director": "Christopher Nolan"
    },
    {
        "id_info": ("MOV-104", 1994),
        "title": "Pulp Fiction",
        "genre": "Crime",
        "rating": 8.9,
        "director": "Quentin Tarantino"
    },
    {
        "id_info": ("MOV-105", 2001),
        "title": "Spirited Away",
        "genre": "Animation",
        "rating": 8.6,
        "director": "Hayao Miyazaki"
    },
    {
        "id_info": ("MOV-106", 2014),
        "title": "Interstellar",
        "genre": "Sci-Fi",
        "rating": 8.7,
        "director": "Christopher Nolan"
    },
    {
        "id_info": ("MOV-107", 1994),
        "title": "The Shawshank Redemption",
        "genre": "Drama",
        "rating": 9.3,
        "director": "Frank Darabont"
    },
    {
        "id_info": ("MOV-108", 2019),
        "title": "Parasite",
        "genre": "Drama",
        "rating": 8.5,
        "director": "Bong Joon-ho"
    }
]

# -------------------------------------------------------------------------
# 3. Create a set containing all unique categories/genres (without loops)
# -------------------------------------------------------------------------
unique_genres = {
    catalogue[0]["genre"],
    catalogue[1]["genre"],
    catalogue[2]["genre"],
    catalogue[3]["genre"],
    catalogue[4]["genre"],
    catalogue[5]["genre"],
    catalogue[6]["genre"],
    catalogue[7]["genre"]
}
print("Unique Genres:", unique_genres)

# -------------------------------------------------------------------------
# 5. At least ten manual retrieval/update operations
# -------------------------------------------------------------------------
# Op 1: Nested indexing into dictionary
print("\nOp 1 - Movie 1 Title:", catalogue[0]["title"])

# Op 2: Chained indexing into the nested tuple (getting release year)
print("Op 2 - Movie 2 Release Year:", catalogue[1]["id_info"][1])

# Op 3: Nested update of an existing value
catalogue[7]["rating"] = 8.6
print("Op 3 - Updated Parasite rating:", catalogue[7]["rating"])

# Op 4: Add a new key-value pair to a dictionary
catalogue[0]["box_office_mil"] = 836.8
print("Op 4 - Added box office field to Inception:", catalogue[0])

# Op 5: Safe dictionary retrieval using .get()
box_office = catalogue[1].get("box_office_mil", "Not Recorded")
print("Op 5 - Safe get on The Matrix box office:", box_office)

# Op 6: Key membership test (`in` dictionary)
has_director = "director" in catalogue[2]
print("Op 6 - Has director key in The Dark Knight?:", has_director)

# Op 7: Membership test (`in` set)
is_action_present = "Action" in unique_genres
print("Op 7 - Is 'Action' genre present?:", is_action_present)

# Op 8: Set method .add() to add a new genre
unique_genres.add("Horror")
print("Op 8 - Genres after adding Horror:", unique_genres)

# Op 9: Dictionary .update() method to modify/add multiple values
catalogue[3].update({"box_office_mil": 213.9, "rated": "R"})
print("Op 9 - Updated Pulp Fiction with .update():", catalogue[3]["rated"])

# Op 10: List method .append() to add a new movie dictionary
catalogue.append({
    "id_info": ("MOV-109", 1993),
    "title": "Jurassic Park",
    "genre": "Adventure",
    "rating": 8.2,
    "director": "Steven Spielberg"
})
print("Op 10 - Appended new movie, total items:", len(catalogue))

# -------------------------------------------------------------------------
# 6. Clean summary printed without using loops
# -------------------------------------------------------------------------
print("\n" + "=" * 65)
print(f"{'ID':<10} {'YEAR':<6} {'TITLE':<25} {'GENRE':<12} {'RATING'}")
print("=" * 65)
print(f"{catalogue[0]['id_info'][0]:<10} {catalogue[0]['id_info'][1]:<6} {catalogue[0]['title']:<25} {catalogue[0]['genre']:<12} {catalogue[0]['rating']}")
print(f"{catalogue[1]['id_info'][0]:<10} {catalogue[1]['id_info'][1]:<6} {catalogue[1]['title']:<25} {catalogue[1]['genre']:<12} {catalogue[1]['rating']}")
print(f"{catalogue[2]['id_info'][0]:<10} {catalogue[2]['id_info'][1]:<6} {catalogue[2]['title']:<25} {catalogue[2]['genre']:<12} {catalogue[2]['rating']}")
print(f"{catalogue[3]['id_info'][0]:<10} {catalogue[3]['id_info'][1]:<6} {catalogue[3]['title']:<25} {catalogue[3]['genre']:<12} {catalogue[3]['rating']}")
print(f"{catalogue[4]['id_info'][0]:<10} {catalogue[4]['id_info'][1]:<6} {catalogue[4]['title']:<25} {catalogue[4]['genre']:<12} {catalogue[4]['rating']}")
print(f"{catalogue[5]['id_info'][0]:<10} {catalogue[5]['id_info'][1]:<6} {catalogue[5]['title']:<25} {catalogue[5]['genre']:<12} {catalogue[5]['rating']}")
print(f"{catalogue[6]['id_info'][0]:<10} {catalogue[6]['id_info'][1]:<6} {catalogue[6]['title']:<25} {catalogue[6]['genre']:<12} {catalogue[6]['rating']}")
print(f"{catalogue[7]['id_info'][0]:<10} {catalogue[7]['id_info'][1]:<6} {catalogue[7]['title']:<25} {catalogue[7]['genre']:<12} {catalogue[7]['rating']}")
print("=" * 65)




#Part G – Stretch Challenges

# -------------------------------------------------------------------------
# 1. Determine duplicates and unique usernames using sets
# -------------------------------------------------------------------------
group_a = ["alice", "bob", "charlie", "david", "emma"]
group_b = ["charlie", "emma", "frank", "grace", "helen"]

set_a = set(group_a)
set_b = set(group_b)

# Duplicates / common to both lists (Intersection)
common_usernames = set_a & set_b
print("Common to both lists:", common_usernames)

# Unique to only one group (Symmetric Difference)
exclusive_usernames = set_a ^ set_b
print("Exclusive to only one group:", exclusive_usernames)

# All unique usernames combined (Union)
all_unique_usernames = set_a | set_b
print("All distinct usernames across both:", all_unique_usernames)


# -------------------------------------------------------------------------
# 2. Nested collection for online course platform (no classes)
# -------------------------------------------------------------------------
online_platform = {
    "platform_name": "LearnSphere",
    "courses": {
        "CS101": {
            "title": "Computer Science Principles",
            "teacher": {
                "name": "Dr. Alan Turing",
                "email": "alan@learnsphere.io"
            },
            "topics": ["Algorithms", "Binary Logic", "Data Structures"],
            "students": [
                {"student_id": "S001", "name": "Maya Lin", "active": True},
                {"student_id": "S002", "name": "Liam Vance", "active": False}
            ]
        },
        "PY201": {
            "title": "Intermediate Python",
            "teacher": {
                "name": "Guido van Rossum",
                "email": "guido@learnsphere.io"
            },
            "topics": ["Decorators", "Generators", "Context Managers"],
            "students": [
                {"student_id": "S001", "name": "Maya Lin", "active": True},
                {"student_id": "S003", "name": "Noah King", "active": True}
            ]
        }
    }
}

# Example access:
teacher_name = online_platform["courses"]["CS101"]["teacher"]["name"]
first_student_cs = online_platform["courses"]["CS101"]["students"][0]["name"]
print("\nCS101 Teacher:", teacher_name)
print("CS101 First Student:", first_student_cs)


# -------------------------------------------------------------------------
# 3. Dictionary-based inventory for five products
# -------------------------------------------------------------------------
inventory = {
    "Mechanical Keyboard": 45,
    "Wireless Mouse": 80,
    "USB-C Cable": 150,
    "27-inch Monitor": 25,
    "Noise-Cancelling Headphones": 30
}

# Update stock values manually
inventory["Wireless Mouse"] -= 12        # 12 mice sold
inventory["27-inch Monitor"] += 10       # 10 monitors restocked

# Calculate total units using .values()
total_units = sum(inventory.values())

print("\nUpdated Inventory:", inventory)
print("Total Units in Stock:", total_units)


# -------------------------------------------------------------------------
# 4. Short comparison in comments: list vs tuple vs set vs dictionary
# -------------------------------------------------------------------------
"""
COLLECTION COMPARISON:

1. LIST:
   - Characteristics: Ordered, mutable (changeable), allows duplicates. Indexed by integers (0, 1, ...).
   - Best fit: A sequence of items where order matters and elements can change, such as a to-do list,
     shopping cart, or chronological timeline of log entries.

2. TUPLE:
   - Characteristics: Ordered, immutable (cannot be changed after creation), allows duplicates. Indexed by integers.
   - Best fit: Fixed records or coordinates that should never be accidentally modified, such as
     (latitude, longitude), RGB color values (255, 128, 0), or database primary key pairs (id, year).

3. SET:
   - Characteristics: Unordered, mutable, does NOT allow duplicate values, highly optimized for membership testing (`in`).
   - Best fit: Removing duplicate entries and checking presence/absence quickly, such as tracking
     visited URLs in a web crawler or filtering distinct email tags.

4. DICTIONARY:
   - Characteristics: Key-value pairs, mutable, keys must be unique and immutable (hashable). Fast lookups by key.
   - Best fit: Structured records representing entities where data is queried by meaningful names,
     such as a user profile ({"username": "...", "email": "...", "age": ...}) or product specs.
"""
