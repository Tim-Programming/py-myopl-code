from fractions import Fraction

class CalculateFractions:
    def __init__(self, fraction: str):
        # Flag, um zu erkennen, ob eine Dezimalzahl verwendet wurde
        self.is_decimal = False
        self.is_symbolic = False

        if '_' in str(fraction):
            self.is_symbolic = True
        elif self.check_float(fraction):
            self.is_decimal = True  # Setze das Flag auf True

        try:
            self.fraction = Fraction(fraction)
        except:
            self.fraction = fraction

    def display_fraction(self) -> str:
        # Ausgabe als Dezimalzahl, wenn das Flag gesetzt ist
        if self.is_decimal:
            return float(self.fraction)  # Gib das Ergebnis als float zurück
        return str(self.fraction)

    def addition_subtraction(self, other_fraction: str, operation: str = "+") -> str:
        if self.check_float(other_fraction):
            self.is_decimal = True  # Setze das Flag auf True
        other = Fraction(other_fraction)
        if operation == "+":
            self.fraction += other
        elif operation == "-":
            self.fraction -= other
        return self.display_fraction()

    def multiplication(self, other_fraction: str) -> str:
        if self.check_float(other_fraction):
            self.is_decimal = True  # Setze das Flag auf True
        other = Fraction(other_fraction)
        self.fraction *= other
        return self.display_fraction()

    def division(self, other_fraction: str) -> str:
        if self.check_float(other_fraction):
            self.is_decimal = True  # Setze das Flag auf True
        other = Fraction(other_fraction)
        if other == 0:
            raise ValueError("Cannot divide by zero.")
        self.fraction /= other
        return self.display_fraction()

    def power(self, exponent: str) -> str:
        if self.check_float(exponent):
            self.is_decimal = True  # Setze das Flag auf True
            exponent = float(Fraction(exponent))
        else:
            print("test")
        try:
            self.fraction = self.fraction ** exponent
        except:
            exponent = float(Fraction(exponent))
            self.fraction = self.fraction ** exponent
        return self.display_fraction()

    def reduce_fraction(self) -> str:
        self.fraction = self.fraction.limit_denominator()  # This is already handled by Fraction
        return self.display_fraction()

    def check_float(self, value) -> bool:  # `self` hinzugefügt
        return isinstance(value, float)
