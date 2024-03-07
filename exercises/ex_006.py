import math


num = int(input('Type a number: '))

nDouble = num*2
nTriple = num*3
# First way to show a Square root of a number
nSquareRoot = num**(1/2)

print('The double is: {}'.format(nDouble))
print('The triple is: {}'.format(nTriple))
# First way to show a Square root of a number
print('The Square root is: {}'.format(nSquareRoot))
# Second way to show a Square root of a number
print('The Square root is: {}'.format(pow(num,(1/2))))
# Third way to show a Square root of a number
print('The Square root is: {}'.format(math.sqrt(num)))