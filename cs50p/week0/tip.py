# TEST CASES
# - $50.00 + 15% = "Leave $7.50"
# - $100.00 + 18% = "Leave $18.00"
# - $15.00 + 25% = "Leave $3.75"

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d = d.replace("$","")
    return float(d)

def percent_to_float(p):
    p = p.replace("%","")
    p = float(p)
    p = p / 100
    return p

main()