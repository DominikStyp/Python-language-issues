# Python language issues
This repo contains **Python practical examples** of certain topics like:
- Classes
  - Inheritance

- Class Methods
  - Method overriding in runtine
  - Abstract methods
  - Static methods
  - var-args methods
  - dictionary-typed arguments in methods
  - mixed method types (var-args + kw-args)
  - using global variables inside methods
  - mutable arguments (changed with each call) in methods like on example below
```python
    def mutableArgsWarn(self, x=[]):
        print "--- mutableArgsWarn ---"
        x.append(1)
        print x
```
- Console usage examples

- Using of following data types:
  - Descriptors
  - Dictionaries
  - Generators
  - Lists
  - Strings
  - Sets
  - Tuples
  
- Formatting date like:
```python
    print datetime.now().strftime("%Y-%m-%d %H:%M:%S")
```

- Parsing date from string:
```python
    print datetime.strptime('Wed, 27 Oct 1770 22:17:00', '%a, %d %b %Y %H:%M:%S')
```

- Determining difference between two dates using **timedelta**
```python
   print "another year:",timedelta(weeks=40, days=84, hours=23, minutes=50, seconds=600)
```

- Debugging using special variables **__builtin__**, **sys**, **inspect**
- Handling and throwing exceptions:
  - using **raise**
  - using **try-except** construct
  - creating user-defined exceptions
  
- File operations
  - examples of common file operations: **read, write, delete, close**
  - saving objects to files in **JSON** format
  - serializing and saving objects
  - example of changing file names using **regular expressions**
  
- Flow Control
  - using **comprehensions**
  - examples of the different loop types: **for in**, **while**
  - using **ternary operator**
  
- Profiling code
  - using of **timeit** module to determine execution time of different variants of 
  - using of **unittest** 

- Regular Expressions
  - matching the pattern using **re.match**
  - finding all occurences of the pattern with **re.findall**
  - iterate over matched results using **re.finditer**
  - splitting string using regular expressions with **re.split**
  - substituting the pattern using **re.sub**
  - display matched results using **match.group** and **match.groups**

- Special Python features
  - Overriding operators using: **__lt__, __le__, __eq__, __ne__, __gt__, __ge__**
  - Using function **decorators** (and simple explanation how this works)
  - Defining **descriptor classes** (If class defines methods __get__, __set__, __delete__ it's called descriptor)
  - different using of **import** statement (wildcards, relative imports)
  - overriding **built-in functions**: example of **how override print function**
  - example of how to override **mathematical operators** behavior in classes

- Python tricks
  - in-place values swapping
  - chaining of comparison operators
  - using generators with **yield** keyword
  - create classes **on-the-fly**
  
- Special class methods examples: **__init__,__new__,__del__,__repr__,__str__,__getattr__,__cal__**

- **Urllib** example usage in **GET and POST** requests (how to easy make get/post requests)
