#!/usr/bin/env python

def main1():

    print "Hello"
    c = float(input("What is the Celsius temperature?"))
    f = (9.0 / 5.0 * c + 32) 
    print("The temp is "), f, (" degrees Fahrenheit.")
    print("Thanks for asking!")
main1()


def main2():
    
    print "Hello again."
    f = float(input("What is the Fahrenheit temperature?"))
    c = (f - 32) * 5.0/9.0
    print("Ah. The temperature is"), c, (" degrees Celsius.")
    print("Now you know.")
main2()
