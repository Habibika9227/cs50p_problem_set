
def main():
    months=[
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december"
]
    while True:
        try:
            date=input("Dates: ").strip()
            
            #Numerical input
            if "/" in date:
                month,day,year=date.split("/")
                month=int(month)
                day=int(day)
                year=int(year)

            # Textual input
            elif "," in date:
                 month_day,year=date.split(",")
                 month_name,day=month_day.lower().split()

                 month=months.index(month_name)+1
                 day=int(day)
                 year=int(year)
                 
            else:
                 raise ValueError
            if not(1<=month<=12 and 1<=day<=31):
                raise ValueError
            print(f"{year:04}-{month:02}-{day:02}")
            break
        except ValueError:
            continue

            
main()            


