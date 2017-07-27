# Correct-input
A tiny library for more convenient input of numbers in console<br/><br/>

Library has functions for input integers and floats. Each function can take a string (text which will be printed in console before input) as an optional argument. Another argument is `err` - message shown in case of incorrect input. This argument has a default value (`Incorrect input, please try again:`) so its specifying is optional.<br/><br/>


`input_int()` returns an integer. This function takes another argument `base` which works similar to standard Python function `int()`. If `base` isn't specified its defaul value is `10`.

`input_float()` returns a floating point number.

`input_num()` returns an integer if entered number is a decimal integer and a floating point number if entered number is a floating point number.<br/><br/>


All these functions has exception handling. So if user inputs invalid data program just asks to input data again.

You can import library using `import` statement or just paste code directly to your own source code.<br/>

**Example of use:**
```
>>> n = input_int("Please enter a number: ", base=16)
Please enter a number: 1a8c
>>> print(n)
6796
```
