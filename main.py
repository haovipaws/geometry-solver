#!/usr/bin/env python3

from sys import argv
import math

answer = []

if argv[1] == "prism":
    answer.append(float(input("[prism mode]: what is the base width ")))
    answer.append(float(input("[prism mode]: what is the base length ")))
    answer.append(float(input("[prism mode]: what is the height ")))

    volume = answer[0]*answer[1]*answer[2]
    surface_area = answer[0]*answer[1]+answer[1]*answer[2]+answer[2]*answer[0]
    print(f'[prism mode]: the volume is: {volume}')
    print(f'[prism mode]: the surface area is: {area}')

elif argv[1] == "cylinder":
    radius = float(input("[cylinder mode]: what is the radius "))
    height = float(input("[cylinder mode]: what is the height "))

    volume = (radius*math.pi**2)*height
    surface_area = 2*radius*math.pi**2+2*math.pi*radius*height
    print(f'[cylinder mode]: the volume is: {volume}')
    print(f'[cylindar mode]: the surface area is: {area}')

elif argv[1] == "pyramid":
    width = float(input("[pyramid mode]: what is the base width "))
    height = float(input("[pyramid mode]: what is the height "))

    print('[pyramid mode]: the volume is: ', (answer[0]*answer[0]*answer[1])/3)
    print('[pyramid mode]: the surface area is: ')

elif argv[1] == "sphere":
    radius = float(input("[sphere mode]: what is the radius"))

    print('[sphere mode]: the volume is: ')
    print('[sphere mode]: the surface area is: ')
