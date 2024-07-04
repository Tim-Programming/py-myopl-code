#######################################
# IMPORTS
#######################################

from math import gcd

#######################################
# BASIC CALCULATION WITH FRACTIONS
#######################################

class Calculate_fractions:
    def __init__(self, fraction):
        self.fraction = fraction
        self.counter, self.denominator = self.seperateFraction(fraction)

    def seperateFraction(self, string):
        fraction = string
        if "/" in str(fraction):
            fraction = fraction.split("/")
            counter = int(fraction[0])
            denominator = int(fraction[1])
        else:
            counter = fraction
            denominator = 1
        return counter, denominator

    def displayFraction(self):
        self.reduceFraction()
        if self.denominator == 1:
            return f'{self.counter}'
        else:
            return f'{self.counter}/{self.denominator}'

    def addition_subtraction(self, other_fraction, operation="+"):
        self.other_counter, self.other_denominator = self.seperateFraction(other_fraction)
        integral_multiple = self.denominator * self.other_denominator
        multiplicant_fraction_1 = integral_multiple // self.denominator
        multiplicant_fraction_2 = integral_multiple // self.other_denominator

        self.counter = self.counter * multiplicant_fraction_1
        self.denominator = self.denominator * multiplicant_fraction_1
        self.other_counter = self.other_counter * multiplicant_fraction_2
        self.other_denominator = self.other_denominator * multiplicant_fraction_2
        if operation == "+":
            self.counter = int(self.counter) + int(self.other_counter)
        elif operation == "-":
            self.counter = int(self.counter) - int(self.other_counter)
    def multiplication(self, other_fraction):
        self.other_counter, self.other_denominator = self.seperateFraction(other_fraction)
        self.counter = int(self.counter) * int(self.other_counter)
        self.denominator = int(self.denominator) * int(self.other_denominator)

    def division(self, other_fraction):
        self.other_counter, self.other_denominator = self.seperateFraction(other_fraction)
        self.multiplication(f'{self.other_denominator}/{self.other_counter}')

    def power(self, exponent):
        counter = self.counter
        denominator = self.denominator
        if exponent == 0:
            self.counter = 1
            self.denominator = 1
        elif exponent >= 1:
            for i in range(0, exponent-1):
                self.counter = self.counter * counter
                self.denominator = self.denominator * denominator
        elif exponent <= -1:
            inversed_counter = self.counter
            inversed_denominator = self.denominator
            for i in range(exponent+1, 0):
                inversed_counter = inversed_counter * counter
                inversed_denominator = inversed_denominator * denominator
            self.counter = inversed_denominator
            self.denominator = inversed_counter
    def reduceFraction(self):
        self.counter = int(self.counter)
        self.denominator = int(self.denominator)
        d = gcd(self.counter, self.denominator)
        self.counter = self.counter // d
        self.denominator = self.denominator // d
        if self.denominator == 1:
            return self.counter
        else:
            return self.counter, self.denominator




#######################################
# TEST
# #####################################

# fraction = Calculate_fractions("7/2")
# fraction.division("4/9")
# print(fraction.displayFraction())
