#!/usr/bin/env python3

from sys import argv

answer = []

if argv[1] == "prism":
    answer.append(float(input("[prism mode]: what is the base width ")))
    answer.append(float(input("[prism mode]: what is the base length ")))
    answer.append(float(input("[prism mode]: what is the height ")))

    print('[prism mode]: the volume is: ', answer[0]*answer[1]*answer[2])
    print('[prism mode]: the surface area is: ', answer[0]*answer[1]+answer[1]*answer[2]+answer[2]*answer[0])

elif argv[1] == "cylinder":
    answer.append(float(input("[cylinder mode]: what is the radius ")))
    answer.append(float(input("[cylinder mode]: what is the height ")))

    print('[cylinder mode]: the volume is: ')
    print('[cylindar mode]: the surface area is: ')

elif argv[1] == "pyramid":
    answer.append(float(input("[pyramid mode]: what is the base width ")))
    answer.append(float(input("[pyramid mode]: what is the height ")))

    print('[pyramid mode]: the volume is: ', (answer[0]*answer[0]*answer[1])/3)
    print('[pyramid mode]: the surface area is: ', answer[0]*answer[0]+answer[0]*answer[1]+answer[1]*answer[0])

elif argv[1] == "sphere":
    answer.append(float(input("[sphere mode]: what is the radius")))

    print('[sphere mode]: the volume is: ')
    print('[sphere mode]: the surface area is: ')
