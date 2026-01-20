def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    dollars=float(dollars)
    percent=float(percent)
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    new_d=d.replace('$','')
    return new_d

    #TODO


def percent_to_float(p):
    new_p=p.replace('%','')
    return float(new_p)/100
    #TODO


main()
