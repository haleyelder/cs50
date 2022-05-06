# breakfast >> 7:00 - 8:00
# lunch >> 12:00 - 13:00
# dinner >> 18:00 - 19:00

def main():
    time = input("What time is it? ")
    hours, minutes = time.split(":")

    timeCheck = float(convert(hours, minutes))

    if timeCheck >= 7.0 and timeCheck <= 8.0:
        print("breakfast time")
    elif timeCheck >= 12.0 and timeCheck <= 13.0:
        print("lunch time")
    elif timeCheck >= 18.0 and timeCheck <= 19.0:
        print("dinner time")


def convert(hours, minutes):
    hours = float(hours)
    minutes = round(float(minutes) / 60, 2)
    return float(hours) + float(minutes)


main()