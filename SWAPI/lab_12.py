# SI 506 2019F - Lab 12
# START LAB EXERCISE 12

import requests

# In this lab exercise, you will practice creating lists and dictionaries
# using comprehensions

# If a problem includes a setup section: Do not modify, delete or otherwise
# ignore the setup code.

# You will save the results to required variables. These variables will be scored
# by the auto grader following your submission.

# Print statements have been provided for you to debug the code.
# You can uncomment them to print values to the screen.

# We provide you with the constant ENDPOINT. Do not modify.

ENDPOINT = "https://swapi.co/api"
resource = '/films/'

# PROBLEM 1 (5 Points)

# In this problem you will
# 1) write a function
# 2) work with the requests module and issue a GET request to SWAPI
# 3) create a new list using a list comprehension

# BEGIN PROBLEM 1 SOLUTION
# 1) Create a function called get_films(url) that makes an HTTP GET request to SWAPI in order
#    to retrieve a list of Star Wars films, each of which is returned as a dictionary.
# 2) Call the function and assign the return value to a variable named films.
# 3) Write a list comprehension that returns a (filtered) list of Star Wars film titles
#    directed by George Lucas. Note: return list of film titles only. Assign the new list
#    to a variable named george_lucas_films.


def get_films(url):
    films_dict = requests.get(url + resource).json()
    return films_dict


films = get_films(ENDPOINT)
george_lucas_films = []

for key, val in films:
    

print(f"films = {films}\n")
# print(f"George Lucas directed films = {george_lucas_films}\n")

# END PROBLEM 1 SOLUTION

# PROBLEM 2 (10 Points)
# In this problem, you will work with the films list created earlier and
# a SWAPI representation of the communications droid C-3PO.

# BEGIN PROBLEM 2 SOLUTION
# 1) Issue an HTTP GET request to SWAPI and retrieve a representation of the droid C-3PO.
# 2) Write a list comprehension that assigns the film title from the films list to each of
#    the films C-3PO has appeared in (match on C-3PO's list of film URLs). Assign the filtered
#    list of film titles to a variable named c_3po_films.

c_3po = None
# print(f"C-3PO = {c_3po}\n")

c_3po_films = None
# print(f"C-3PO films = {c_3po_films}\n")

# END PROBLEM 2 SOLUTION

# PROBLEM 3 (10 Points)
# In this problem, you will
# 1) employ a tuple of named keys to filter a dictionary of key-value pairs
# 2) Write a dictionary comprehension to create a filtered list of C-3PO key-value pairs
#    using the tuple to filter on the c_3po dictionary keys.

# BEGIN PROBLEM 3 SOLUTION
# 1) Create a tuple named DROID_KEYS with the following key name items (same order):
#    'name', 'height', 'mass', 'skin_color', 'eye_color', 'birth_year'
# 2) Write a dictionary comprehension that returns only the c_3pO key-value pairs that
#    match on the DROID_KEYS. Assign the return value to the variable named c_3pO_filtered.

# HINT: when writing the dictionary comprehension make use of the .keys() method to return
#       a list of c_3po dictionary keys.

DROID_KEYS = (
    'name', 'height', 'mass', 'skin_color', 'eye_color', 'birth_year'
)
c_3po_filtered = {key:c_3po[key] for key in DROID_KEYS if c_3po.keys() in DROID_KEYS}
# print(f"C-3PO filtered = {c_3po_filtered}\n")

# END PROBLEM 3 SOLUTION
# END LAB EXERCISE
