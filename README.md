# Correct-input
Small module for more convenient organization of numbers input in console

This module has functions for input integers and floats. Each function can take a string (text which will be printed in console before input) as an optional argument.

input_int() returns an integer (this function takes another optional argument 'base' and in this case works similar to standard Python function int() )

input_float() returns a floating point number

input_num() returns an integer if entered number is a decimal integer and a floating point number if entered number is a floating point number

All these functions has exception handling. So if user inputs invalid data program just asks to input data again.

You can import module using 'import' statement or just paste code directly to your own source code.

**Example of use:**

>>> n = input_int("Please enter a number: ", base=16)

Please enter a number: 1a8c

>>> print(n)

6796
