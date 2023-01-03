#!/usr/bin/env python3

from sys import argv
import math

answer = []

volume = "unknown"
surface_area = "unknown"

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

elif argv[1] == "cylinder":
    radius = float(input("[cylinder mode]: what is the radius "))
    height = float(input("[cylinder mode]: what is the height "))

    volume = (radius * math.pi ** 2) * height
    surface_area = 2 * radius * math.pi ** 2 + 2 * math.pi * radius * height
    
    # Display answer
    print(f'[cylinder mode]: the volume is: {volume}')
    print(f'[cylindar mode]: the surface area is: {surface_area}')

elif argv[1] == "pyramid":
    width = float(input("[pyramid mode]: what is the base width "))
    height = float(input("[pyramid mode]: what is the height "))

    # Calculations
    volume = (width * width * height) / 3
    # TODO surface area

    # Display answer
    print(f'[pyramid mode]: the volume is: {volume}')
    print(f'[pyramid mode]: the surface area is: {surface_area}')

elif argv[1] == "sphere":
    radius = float(input("[sphere mode]: what is the radius"))

    # Calculations
    # TODO: add calculations or pretend to

    # Display answer
    print(f'[sphere mode]: the volume is: {volume}')
    print(f'[sphere mode]: the surface area is: {surface_area}')
