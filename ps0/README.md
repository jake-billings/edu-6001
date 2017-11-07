# Problem Set 1 #

#### Write a program that does the following in order: ####

1. Asks the user to enter a number "x"
2. Asks the user to enter a number "y"
3. Prints out number "x", raised to the power "y"
4. Prints out the log (base 2) of "x"

```python
# Import logarithms from the math package
from math import log

# 1
x = input('Please enter x: ')

# 2
y = input('Please enter y: ')

# 3
print '%s to the power of %s is %s' % (x, y, x**y)

# 4
print 'log(%s)/log(2) is %s' % (x, log(x,2))
```