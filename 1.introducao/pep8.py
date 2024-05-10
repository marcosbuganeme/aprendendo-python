"""
PEP8 - Python Enhancement Proposal

Proposals for the improvement of the Python language

The Zem of Python

import this

print(this)

[1] - Use Camel Case for classes;

class Calculator:
  pass

class CalculatorScientific:
  pass

[2] - Use lowercase for functions or variables;

def sum():
  pass

def sum_two():
  pass

number = 4
number_imper = 5

[3] - Use 4 spaces for indentation! (Not use tab)
if 'a' in 'banana':
    print('There is a in banana')

[4] - Blank lines;
- Separate functions and definitions with two blank lines;
- Methods and classes within a class should be separated by a single blank line;

[5] - Imports
- Imports should be done in separate lines;

#import error
import sys, os

#import correct
import sys
import os

#Not problem with:
from types import StringType, ListType

#if there are many imports from the same package, it is recommended to do:

from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

#imports should be placed at the beginning of the file, after any comments or documentation and before global variables and constants.


"""

