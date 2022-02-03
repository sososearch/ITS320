#------------------------------------------------------------------------
# Program Name: Working with Python Classes
# Author: Musung Kim
# Date: 1/24/2021
#------------------------------------------------------------------------
# Pseudocode: This program will take two complex numbers and print the result of their addition,
# subtraction, multiplication, division, and modulus operations.

#------------------------------------------------------------------------
# Program Inputs: Real and imaginary part of a number separated by a space
# Program Outputs: For two complex numbers and the output should be in the following sequence:
# C + D
# C - D
# C * D
# C / D
# mod(C)
# mod(D)
#------------------------------------------------------------------------

import math

# define different classes
class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        real = self.real + no.real
        imaginary = self.imaginary + no.imaginary
        return Complex(real, imaginary)

    def __sub__(self, no):
        real = self.real - no.real
        imaginary = self. imaginary - no.imaginary
        return Complex(real, imaginary)

    def __mul__(self, no):
        real = (self.real * no.real - self.imaginary * no.imaginary)
        imaginary = (self.real * no.imaginary + self.imaginary * no.real)
        return Complex(real, imaginary)

    def __truediv__(self, no):
        C_square = no.real * no.real
        D_square = no.imaginary * no.imaginary
        deno = C_square + D_square
        real = (self.real * no.real + self.imaginary * no.imaginary) / (deno)
        imaginary = (self.imaginary * no.real - self.real * no.imaginary) / (deno)
        return Complex(real, imaginary)

    def mod(self):
        real = math.sqrt((self.real * self.real + self.imaginary * self.imaginary))
        return Complex(real, 0)

    def __str__(self):
        real = "%.2f" % self.real
        imaginary = "%.2f" % self.imaginary
        if (self.imaginary) >= 0:
            result = (str(real) + '+' + str(imaginary) + 'i')
        else:
            result = (str(real) + '' + str(imaginary)+ 'i')
        return result

if __name__ == '__main__':
    C = map(float, input('Enter 1st set of complex # (real & imaginary numbers separated by a space): ').split())
    D = map(float, input('Enter 2nd set of complex # (real & imaginary numbers separated by a space): ').split())
    x = Complex(* C)
    y = Complex(* D)
    print ('\n'.join(map(str, [x.__add__(y), x.__sub__(y), x.__mul__(y), x.__truediv__(y), x.mod(), y.mod()])))

