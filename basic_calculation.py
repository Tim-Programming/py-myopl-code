#######################################
# IMPORTS
#######################################

from fractions import Fraction

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
            try:
                # Try to convert to Fraction first
                frac = Fraction(fraction)
                counter = frac.numerator
                denominator = frac.denominator
            except (ValueError, TypeError):
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
        is_fraction, result_counter, result_denominator = self.convert_fraction_into_float(other_fraction, operation)
        if is_fraction is None:
            self.counter = result_counter
            self.denominator = result_denominator
            return self.counter
            
        # Use Fraction for the calculation
        a = Fraction(self.counter, self.denominator)
        b = Fraction(*self.seperateFraction(other_fraction))
        
        result = a + b if operation == "+" else a - b
        self.counter = result.numerator
        self.denominator = result.denominator

    def multiplication(self, other_fraction):
        is_fraction, result_counter, result_denominator = self.convert_fraction_into_float(other_fraction, "*")
        if is_fraction is None:
            self.counter = result_counter
            self.denominator = result_denominator
            return self.counter
            
        # Use Fraction for the calculation
        a = Fraction(self.counter, self.denominator)
        b = Fraction(*self.seperateFraction(other_fraction))
        
        result = a * b
        self.counter = result.numerator
        self.denominator = result.denominator

    def division(self, other_fraction):
        is_fraction, result_counter, result_denominator = self.convert_fraction_into_float(other_fraction, "/")
        if is_fraction is None:
            self.counter = result_counter
            self.denominator = result_denominator
            return self.counter
            
        # Use Fraction for the calculation
        a = Fraction(self.counter, self.denominator)
        b = Fraction(*self.seperateFraction(other_fraction))
        
        result = a / b
        self.counter = result.numerator
        self.denominator = result.denominator

    def power(self, exponent):
        is_fraction, result_counter, result_denominator = self.convert_fraction_into_float(exponent, "^")
        if is_fraction is None:
            self.counter = result_counter
            self.denominator = result_denominator
            return self.counter
        
        # Use Fraction for integer exponents
        a = Fraction(self.counter, self.denominator)
        result = a ** int(exponent)
        self.counter = result.numerator
        self.denominator = result.denominator

    def reduceFraction(self):
        if isinstance(self.counter, float):
            return float(self.counter)
        
        # Use Fraction to reduce
        frac = Fraction(self.counter, self.denominator)
        self.counter = frac.numerator
        self.denominator = frac.denominator
        
        if self.denominator == 1:
            return self.counter
        else:
            return self.counter, self.denominator

    def convert_fraction_into_float(self, other_fraction, operation):
        # Handle cases where either value is a floating point number
        if "." not in str(self.fraction) and "." not in str(other_fraction):
            return True, self.counter, self.denominator
        
        # Handle floating point operations
        if "." in str(self.fraction) or "." in str(other_fraction):
            try:
                a = float(self.fraction)
                b = float(other_fraction)
                
                if operation == "+": result = a + b
                elif operation == "-": result = a - b
                elif operation == "*": result = a * b
                elif operation == "/": result = a / b
                elif operation == "^": result = pow(a, b)
                
                return None, result, 1
            except:
                # Handle mixed fraction and float operations
                if "." in str(self.fraction):
                    a = float(self.fraction)
                    other_counter, other_denominator = self.seperateFraction(other_fraction)
                    b = other_counter / other_denominator
                    
                    if operation == "+": result = a + b
                    elif operation == "-": result = a - b
                    elif operation == "*": result = a * b
                    elif operation == "/": result = a / b
                    elif operation == "^": result = pow(a, b)
                    
                    return None, result, 1
                else:
                    a = self.counter / self.denominator
                    b = float(other_fraction)
                    
                    if operation == "+": result = a + b
                    elif operation == "-": result = a - b
                    elif operation == "*": result = a * b
                    elif operation == "/": result = a / b
                    elif operation == "^": result = pow(a, b)
                    
                    return None, result, 1
        
        return True, self.counter, self.denominator