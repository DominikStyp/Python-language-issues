# Python language issues
This repo contains **Python practical examples** of certain topics like:
- <a href="./classesIssues">Classes</a>
  - Inheritance

- <a href="./classesIssues">Class Methods</a>
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
- <a href="./consoleUsing/consoleIssues.py">Console usage examples</a>

- <a href="./dataTypes">Using of different data types</a>:
  - <a href="./dataTypes/DescriptorsExample.py">Descriptors example1</a>, 
  - <a href="./dataTypes/DescriptorsExample2.py">Descriptors example2</a>
  - <a href="./dataTypes/Dictionaries.py">Dictionaries</a>
  - <a href="./dataTypes/Generators.py">Generators</a>
  - <a href="./dataTypes/Lists.py">Lists</a>
  - <a href="./dataTypes/Strings.py">Strings</a>
  - <a href="./dataTypes/Sets.py">Sets</a>
  - <a href="./dataTypes/Tuples.py">Tuples</a>
  - <a href="./dataTypes/EnforceMethodParamType.py">Enforcing method parameter type</a>
  
- <a href="./dateAndTimeOperations/formattingDate.py">Formatting date</a>:
```python
    print datetime.now().strftime("%Y-%m-%d %H:%M:%S")
```

- <a href="./dateAndTimeOperations/parsingDateFromString.py">Parsing date from string</a>:
```python
    print datetime.strptime('Wed, 27 Oct 1770 22:17:00', '%a, %d %b %Y %H:%M:%S')
```

- <a href="./dateAndTimeOperations/timedelta.py">Determining difference between two dates</a> using **timedelta**
```python
   print "another year:",timedelta(weeks=40, days=84, hours=23, minutes=50, seconds=600)
```

- <a href="./debugging/specialVariables.py">Debugging using special variables</a> **__builtin__**, **sys**, **inspect**
- <a href="./exceptions/">Handling and throwing exceptions</a>:
  - using **raise**
  - <a href="./exceptions/ExampleHandlers.py">using **try-except** construct</a>
  - <a href="./exceptions/UserDefinedExceptions.py">creating user-defined exceptions</a>
  
- <a href="./fileOperations/">File operations</a>
  - examples of common file operations: **read, write, delete, close**
  - saving objects to files in **JSON** format
  - serializing and saving objects
  - example of changing file names using **regular expressions**
  
- <a href="./flowControl">Flow Control</a>
  - using **comprehensions**
  - examples of the different loop types: **for in**, **while**
  - using **ternary operator**
  
- <a href="./profilingCode">Profiling code</a>
  - using of **timeit** module to determine execution time of different variants of 
  - using of **unittest** 

- <a href="./regularExpressions/SimpleExamples.py">Regular Expressions</a>
  - matching the pattern using **re.match**
  - finding all occurences of the pattern with **re.findall**
  - iterate over matched results using **re.finditer**
  - splitting string using regular expressions with **re.split**
  - substituting the pattern using **re.sub**
  - display matched results using **match.group** and **match.groups**

- <a href="./specialPythonFeatures">Special Python features</a>
  - <a href="./specialPythonFeatures/ComparableObjects.py">Overriding operators</a> using: **__lt__, __le__, __eq__, __ne__, __gt__, __ge__**
  - <a href="./specialPythonFeatures/Decorators.py">Using function **decorators**</a> (and simple explanation how this works)
  - <a href="./specialPythonFeatures/DescriptorDefinition.py">Defining **descriptor classes**</a> (If class defines methods __get__, __set__, __delete__ it's called descriptor)
  - <a href="./specialPythonFeatures/ImportIssues.py">different using of **import** statement</a> (wildcards, relative imports)
  - <a href="./specialPythonFeatures/OverrideBuiltInFunctions.py">overriding **built-in functions**</a>: example of **how override print function**
  - <a href="./specialPythonFeatures/Point.py">example of how to override **mathematical operators**</a> behavior in classes

- <a href="./specialPythonFeatures/PythonTricks.py">Python tricks</a>
  - in-place values swapping
  - chaining of comparison operators
  - using generators with **yield** keyword
  - create classes **on-the-fly**
  
- <a href="./specialPythonFeatures/SpecialMethods.py">Special class methods</a> examples: **__init__,__new__,__del__,__repr__,__str__,__getattr__,__cal__**

- <a href="./Urllib/GetAndPostQueries.py">**Urllib** example usage in **GET and POST** requests</a> (how to easy make get/post requests)
