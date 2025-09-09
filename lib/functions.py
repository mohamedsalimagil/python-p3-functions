#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")
    

def greet(name="Naureen"):
    print(f"Hello, {name}!")
    
    

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
    
greet_with_default()
greet_with_default("Sunny")



def add(num1, num2):
    return num1 + num2

sum_result = add(45, 55)
print(sum_result)    

def halve(number):
    if not isinstance(number, (int, float)):
        return None
    return number / 2
