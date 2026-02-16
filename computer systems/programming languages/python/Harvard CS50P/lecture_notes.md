python's official documentation：docs.python.org
# functions & variables
## print
```python
print("Hello, world")   # no ";"

name = input("What's your name? ")   # input() expects text input

# in one line
print("Hello, " + name)   # one argument
# use comma to seperate, automatically insert a space
print("Hello,", name)   # two argument

# in two lines
print("Hello, ")
print(name)   
```
print() have hidden parameters: sep = ' ' and end = '\n'
```python
print("hello, ", end = "")   # nothing at the end
print(name)
# output: hello, adven

print("hello, ", name, sep = "")   # no auto space
```
always use double quotes in python
"sep", "end" are name parameters, can pass them in the end
escape sequences 转义序列 are the same
```python
print(f"hello, {name}")   # f for format

# functions in str itself
str = str.strip()   # remove whitespace on the left and right from str
str = str.capitalize()   # capitalize the first letter
str = str.title()   # capitalize the first letter of each word
first, second = str.split(" ")  # split the str when " "
```

## types of data 
```python
# when don't want to treat input as str
x = int(input("what is x? "))   # int() is a function
y = int(input("what is y? "))
print(x + y)

z = round(x / y, 2)   # number of digits after the decimal point 
print(f"{z:.2f}")   # forma same as above
print(f"{z:,}")   # format like 1,000
```
python has no bound on "int"

## define functions
```python
def hello():
    print("Hello, ", end = "")
name = input("What is your name? ")
hello()
print(name)

def hello(to = "world"):
    print("hello,", to)
hello()
name = input("What's your name? ")
hello(name)
# just like the "end" and "sep"
```
```python
# a standard way to write codes in a right order
def main():
    name = input("What's your name? ")
    hello(name)
def hello(to = "world"):
    print("hello,", to)
main()   # call the main part at the bottom
```
```python
# return values, no side effects
def main():
    x = int(input("what is x? "))
    print("x squared is", square(x))
def square(n):
    return n * n
main()
```

# conditionals
## grammer
```python
if x > y: 
    print("bigger")
elif x < y:
    print("smaller")
else: 
    print("equal")

def is_even(n):
    return (n % 2 == 0)  
# if a expression already returns a bool answer, use it directly
```

## match
just like "switch" in c++
```python
name = input("What's your name?")
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
# no "default" or "break", just "_" at the end
```

# loops
## while
```python
i = 0
while i < 3:
    print("meow")
    i += 1
```

## for
```python
for i in [0, 1, 2]:
    print("meow")

for i in range(3):
    # range(n) means 0 to (n - 1)
    print("meow")

# when the counter is not used
for _ in range(3)
```
```python
# a pythonic version
while True:
    n = int(input("What's n?"))
    if n > 0:
        break
for _ in range(n):
    print("meow")
```

## list
```python
students = ["Hermoine", "Harry", "Ron"]
for student in students:
    print(student)

for i in range(len(students)):
    print(students[i])
```

## dict
two-dimensional, like a dictionary, key and value
```python
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

print(students["Hermione"])

# a special pythonic feature
for student in students:
    print(student, students[student], sep = ", ")
```
more dimensions, dictionaries in list
```python
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "otter"}
    {"name": "Harry", "house": "Gryffindor", "patronus": "stag"}
    {"name": "Ron", "house": "Gryffindor", "patronus": "terrior"}
    {"name": "Draco", "house": "Slytherin", "patronus": None}
    # None is a keyword in python, meaning nothing
]

for student in students:
    print(student["name"])  # calls for the dict
```

# exceptions
```python
# a pythonic method
try:
    x = int(input("what's x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")
# ValueError: when a function is not getting the right type of parameter
```
```python
try:
    x = int(input("what's x? "))   # less things in try is better
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")
```
```python 
# a more friendly program
while True:
    try:
        x = int(input("What's x?"))
        break
    except ValueError:
        print("x is not a integer")

print(f"x is {x}")
```
```python
def main():
    x = get_int()
    print(x)

def get_int():
    while True:
        try:
            return int(input("What's x?"))
        except ValueError:
            pass

main()
```

# libraries
## random
keyword to access to modules, import
```python
# flipping a coin
import random
coin = random.choice(["heads", "tails"])
print(coin)
# when having a scope, can collide on names 

from random import choice
coin = choice(["heads", "tails"])
print(coin)
```
```python
import random
number = random.ranint(1, 10)  
# random number between 1 and 10
print(number)

cards = ["jack", "qween", "king"]
random.shuffle(cards)
for card in cards:
    print(card)
```

## statistics
many function about statistics
```python
import statistics
print(statistics.mean([100, 90]))  # average
```

## sys
there is a variable in sys module, sys.argv (arugument vector, a list)
the list of all of the words that human type in at their prompt before hitting enter
```python
import sys
print("hello, my name is", sys.argv[1])  
# expecting the user to type in their name when running the program 
# index 0 stores the name of the file
# if typing nothing, accessing to index 0 will call IndexError
```
```python
import sys
# check for errors
if len(sys.argv) < 2:
    sys.exit("Too few arguments")   # exit from my program
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

# if there is no errors, don't hide in a else clause
print("hello, my name is", sys.argv[1])
```
```python
import sys
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
for arg in sys.argv[1:]:     # slice
    print("hello , my name is", arg)
```

## response
get responses from browser
```python
import requests
import sys
import json
if len(sys.argv) != 2:
    sys.exit()
response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(json.dumps(response.json(), indent=2))
# json module can help format the json text to a readable style 
```

# own module
if having two file in the same directory , we can inport one in the other
```python
# sayings.py
def main():
    name = input()
def hello(name):
    print(f"hello, {name}")
def goodbye(name):
    print(f"goodbye, {name}")
# only run main when running this program
if __name__ == "__main__":
    main()

# say.py
from sayings import hello
import sys
if len(sys.argv) == 2:
    hello(sys.argv[1])
```

# Unit Tests
When using a function, normally add this at the end of the program
```python
if __name__ == "__main__":
    main()
```
to ensure when i import my function "main" won't call itself
When testing a function, make another file 
```python
# test_calculator.py
from calculator import square

def main():
    test_square()

def test_square():
    if square(2) != 4:
        print("2 squared was not 4")
    if square(3) != 9:
        print("3 squared was not 9")

if __name == "__main__":
    main()
```
### assert
```python
# test_calculator.py
from calculator import square

def main():
    test_square()

def test_square():
    assert square(2) == 4
    assert square(3) == 9
# if it's wrong, end up in AssertError

if __name == "__main__":
    main()
```
```python
def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared was not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared was not 9")
```
## pytest
a third-party program one can install, which can automate the testing of one's code
```python
# test_cal.py
def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(0) == 0
# nothing more is needed
```
break down the tests into mutiple tests to better know what is wrong
```python
import pytest 
def test_positive():
    assert square(3) == 9
def test_negative():
    assert square(-2) == 4
def test_zero():
    assert square(0) == 0
# even if something is wrong, all will be tested

def test_str():
    with pytest.raises(TypeError):
        square("cat")
# meaning when inputting a string "cat", assert it will raise TypeError
```
Best not to have side effects in a function, especially if we want to test it
```python
# hello.py
def main():
    name = input("What's your name?")
    print(hello(name))

def hello(to = "world"):
    return f"hello, {to}"
    # don't use "print", side effects are uncheckable
 
if __name__ == "__main__":
    main()

# test_hello.py
from hello import hello
def test_default():
    assert hello() == "hello, world"
def test_argument():
    assert hello("David") == "hello, David"

# run "pytest test_hello.py" in the terminal
```
## packages
Telling python to treat that folder as a package not just a module
file __init__.py is a visual indicator to python 
```python
# mkdir test
# test_hello.py
# __init__.py
# pytest test
```
