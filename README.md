# Geometry Problem Solver 
I made this command line program for my geometry class during quarentine, and it was useful to not have to solve brain-numbing problems about a shapes surface area and volume over and over. It was never finished because I finished the class before i could complete the solver.

### Imports
```py 
from sys import argv
import math
```
I imported the `argv` library to collect command line arguements passed to the program (e.g prism or sphere)

### Code
I am using the prism code as an example, but either of the completed ones could be used for this
```py
if argv[1] == "prism":
    width = float(input("[prism mode]: what is the base width "))
    length = float(input("[prism mode]: what is the base length "))
    height = float(input("[prism mode]: what is the height "))

    # Calculations
    volume = width * length * height
    surface_area = width * length + length * height + height * width
    
    # Display answer
    print(f'[prism mode]: the volume is: {volume}')
    print(f'[prism mode]: the surface area is: {surface_area}')
```
This is the main part of the program, the `if argv[1]` statement checks what shape you want the area and volume of, and the `float(input("[prism mode]: what is the base width"))` lines collect the dimensions of the shape. the next few lines are self explanatory as they just solve based on the shape type, and the last two lines just print out the solutions.
