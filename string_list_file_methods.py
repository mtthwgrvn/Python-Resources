#Python String, List, File Methods pulled from w3schools.com as a quick resource for my SI 506 Midterm exam

#  Python String methods

Python has a set of built-in methods that you can use on strings.

Note: All string methods returns new values. They do not change the original string.

Method	        Description
capitalize()	  Converts the first character to upper case
casefold()	    Converts string into lower case
center()	      Returns a centered string
count()	        Returns the number of times a specified value occurs in a string
encode()	      Returns an encoded version of the string
endswith()	    Returns true if the string ends with the specified value
expandtabs()	  Sets the tab size of the string
find()	        Searches the string for a specified value and returns the position of where it was found
format()	      Formats specified values in a string
format_map()	  Formats specified values in a string
index()	        Searches the string for a specified value and returns the position of where it was found
isalnum()	      Returns True if all characters in the string are alphanumeric
isalpha()	      Returns True if all characters in the string are in the alphabet
isdecimal()	    Returns True if all characters in the string are decimals
isdigit()	      Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	      Returns True if all characters in the string are lower case
isnumeric()	    Returns True if all characters in the string are numeric
isprintable()	  Returns True if all characters in the string are printable
isspace()	      Returns True if all characters in the string are whitespaces
istitle()	      Returns True if the string follows the rules of a title
isupper()	      Returns True if all characters in the string are upper case
join()	        Joins the elements of an iterable to the end of the string
ljust()	        Returns a left justified version of the string
lower()	        Converts a string into lower case
lstrip()	      Returns a left trim version of the string
maketrans()	    Returns a translation table to be used in translations
partition()	    Returns a tuple where the string is parted into three parts
replace()	      Returns a string where a specified value is replaced with a specified value
rfind()	        Searches the string for a specified value and returns the last position of where it was found
rindex()	      Searches the string for a specified value and returns the last position of where it was found
rjust()	        Returns a right justified version of the string
rpartition()	  Returns a tuple where the string is parted into three parts
rsplit()	      Splits the string at the specified separator, and returns a list
rstrip()	      Returns a right trim version of the string
split()	        Splits the string at the specified separator, and returns a list
splitlines()	  Splits the string at line breaks and returns a list
startswith()	  Returns true if the string starts with the specified value
strip()	        Returns a trimmed version of the string
swapcase()	    Swaps cases, lower case becomes upper case and vice versa
title()	        Converts the first character of each word to upper case
translate()	    Returns a translated string
upper()	        Converts a string into upper case
zfill()	        Fills the string with a specified number of 0 values at the beginning


# Python List methods

#Python has a set of built-in methods that you can use on lists/arrays.

#Method	    Description
append()	  Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	  Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	  Adds an element at the specified position
pop()	      Removes the element at the specified position
remove()	  Removes the first item with the specified value
reverse()	  Reverses the order of the list
sort()	    Sorts the list



# Python Built-in functions

Python has a set of built-in functions.

Function	   Description
abs()	      Returns the absolute value of a number
all()	      Returns True if all items in an iterable object are true
any()	      Returns True if any item in an iterable object is true
ascii()	      Returns a readable version of an object. Replaces none-ascii characters with escape character
bin()	      Returns the binary version of a number
bool()	      Returns the boolean value of the specified object
bytearray()	  Returns an array of bytes
bytes()	      Returns a bytes object
callable()	  Returns True if the specified object is callable, otherwise False
chr()	      Returns a character from the specified Unicode code.
classmethod()	Converts a method into a class method
compile()	  Returns the specified source as an object, ready to be executed
complex()	  Returns a complex number
delattr()	  Deletes the specified attribute (property or method) from the specified object
dict()	      Returns a dictionary (Array)
dir()	      Returns a list of the specified object's properties and methods
divmod()	  Returns the quotient and the remainder when argument1 is divided by argument2
enumerate()	  Takes a collection (e.g. a tuple) and returns it as an enumerate object
eval()	      Evaluates and executes an expression
exec()	      Executes the specified code (or object)
filter()	  Use a filter function to exclude items in an iterable object
float()	      Returns a floating point number
format()	  Formats a specified value
frozenset()	  Returns a frozenset object
getattr()	  Returns the value of the specified attribute (property or method)
globals()	  Returns the current global symbol table as a dictionary
hasattr()	  Returns True if the specified object has the specified attribute (property/method)
hash()	      Returns the hash value of a specified object
help()	      Executes the built-in help system
hex()	      Converts a number into a hexadecimal value
id()	      Returns the id of an object
input()	      Allowing user input
int()	      Returns an integer number
isinstance()	Returns True if a specified object is an instance of a specified object
issubclass()	Returns True if a specified class is a subclass of a specified object
iter()	      Returns an iterator object
len()	      Returns the length of an object
list()	      Returns a list
locals()	  Returns an updated dictionary of the current local symbol table
map()	      Returns the specified iterator with the specified function applied to each item
max()	      Returns the largest item in an iterable
memoryview()  Returns a memory view object
min()	      Returns the smallest item in an iterable
next()	      Returns the next item in an iterable
object()	  Returns a new object
oct()	      Converts a number into an octal
open()	      Opens a file and returns a file object
ord()	      Convert an integer representing the Unicode of the specified character
pow()	      Returns the value of x to the power of y
print()	      Prints to the standard output device
property()	  Gets, sets, deletes a property
range()	      Returns a sequence of numbers, starting from 0 and increments by 1 (by default)
repr()	      Returns a readable version of an object
reversed()	  Returns a reversed iterator
round()	      Rounds a numbers
set()	      Returns a new set object
setattr()	  Sets an attribute (property/method) of an object
slice()	      Returns a slice object
sorted()	  Returns a sorted list
@staticmethod()	    Converts a method into a static method
str()	      Returns a string object
sum()	      Sums the items of an iterator
super()	      Returns an object that represents the parent class
tuple()	      Returns a tuple
type()	      Returns the type of an object
vars()	      Returns the __dict__ property of an object
zip()	      Returns an iterator, from two or more iterators



# Python File methods

Python has a set of methods available for the file object.

Method	         Description
close()	        Closes the file
detach()	      Returns the separated raw stream from the buffer
fileno()	      Returns a number that represents the stream, from the operating system's perspective
flush()	        Flushes the internal buffer
isatty()	      Returns whether the file stream is interactive or not
read()	        Returns the file content
readable()	    Returns whether the file stream can be read or not
readline()	    Returns one line from the file
readlines()	    Returns a list of lines from the file
seek()	        Change the file position
seekable()	    Returns whether the file allows us to change the file position
tell()	        Returns the current file position
truncate()	    Resizes the file to a specified size
writeable()	    Returns whether the file can be written to or not
write()	        Writes the specified string to the file
writelines()	  Writes a list of strings to the file
