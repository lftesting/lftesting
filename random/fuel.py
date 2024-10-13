from fractions import Fraction

def main():
    x = get_percentage()
    if x <= 1:
        print("E")
    elif x >= 99:
        print("F")
    else:
        print(f"{x}%")


def get_percentage():
    while True:
        try:    
            fraction_input = Fraction(input("Fraction: ")) 
            x = fraction_input.numerator
            y = fraction_input.denominator
            
            if x > y:
                continue
            if y == 0:
                continue
            
            percentage = round((x/y) * 100)
            return percentage
        except (ValueError, ZeroDivisionError):
            continue


main()
