# TEST CASES
# - 9/8/1636 >> 1636-09-08
# - September 8, 1636 >> 1636-09-08
# - 23/6/1912 >> reprompt
# - December 80, 1980 >> reprompt
# if no comma in str option or spaces around / , reprompt
# assume every month has no more than 31 days, no need to validate specific 28,29,30, or 31

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    formattedDate = validate_date()
    print(formattedDate)

def validate_date():
    date = input("Date: ")

    while True:
        try:
            if (',') in date and ("/") not in date:
                date = date.split(', ')
                year = date[1]
                monthDay = date[0].split(" ")
                day = monthDay[1].zfill(2)
                monthIndex = months.index(monthDay[0]) + 1

                #reprompt if days out of bounds
                if int(day) > 31:
                    date = input("Date: ")
                formatted = f"{year}-{monthIndex:02}-{day:02}"
                return formatted

            elif ('/') in date:
                if date.isalnum():
                    date = input("Date: ")

                date = date.split('/')

                # reprompt if spaces
                for x in date:
                    if " " in x:
                        date = input("Date: ")

                month = date[0].zfill(2)
                day = date[1].zfill(2)
                year = date[2]

                # reprompt if out of bounds
                if int(day) > 31 or int(month) > 12:
                    date = input("Date: ")

                formatted = f"{year}-{month}-{day}"
                return formatted

        except ValueError:
            date = input("Date: ")
        else:
            continue

main()
