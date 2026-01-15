


def main():
    dollars=dollars_to_float(input("how much was the meal? "))
    percent=percent_to_float(input("what percentage would you like to tip? " ))
    tip=dollars*percent
    print(f"leave ${tip:.2f}")

def dollars_to_float(d):
    d=d.replace("$", "")
    z=float(d)
    return z    






def percent_to_float(p):
    p=p.replace("%", "")
    result=float(p)/100

    return result

main()