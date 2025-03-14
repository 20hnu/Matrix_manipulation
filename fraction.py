class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    def __add__(self,first):
        num = first.numerator * self.denominator + self.numerator * first.denominator
        denom = first.denominator * self.denominator
        return Fraction(num, denom)
    
    def __sub__(self,first):
        num =self.numerator * first.denominator - first.numerator * self.denominator 
        denom = first.denominator * self.denominator
        return Fraction(num, denom)
    
    def __mul__(self, first):
        num = first.numerator * self.numerator
        denom = first.denominator * self.denominator
        return Fraction(num, denom)
    
    def __truediv__(self, first):
        num = first.numerator * self.denominator
        denom = first.denominator * self.numerator
        return Fraction(num, denom)
    
    
if __name__ == "__main__":
    f = Fraction(1, 2)
    g = Fraction(3, 4)
    print(f)
    print(g)
    print(f + g)
    print(f - g)
    print(f * g)
    print(f / g)

    