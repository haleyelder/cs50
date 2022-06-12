import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    try:
        # 9AM - 5PM
        if "-" in s:
            raise ValueError

        s = s.split(" to ")

        listTime = []

        for i in s:
            # if time has colon
            time = re.search("\d+:\d+",i)

            if time:
                ampmSplit = i.split(" ")
                # 09:00 to 17:00
                valCheck = time[0].split(":")
                if int(valCheck[0]) >= 13:
                    raise ValueError

                if "AM" in ampmSplit:
                    firstNum = time[0].split(":")
                    digit = int(firstNum[0])

                    if digit == 12:
                        am = f"00:{firstNum[1]}"
                        listTime.append(am)
                    else:
                        am = f"{digit:02}:{firstNum[1]}"
                        listTime.append(am)

                    if int(firstNum[1]) > 59:
                        raise ValueError

                if "PM" in ampmSplit:
                    firstNum = time[0].split(":")

                    if firstNum[0] == "12":
                        pm = f"12:{firstNum[1]}"
                        listTime.append(pm)
                    else:
                        eveConvert = int(firstNum[0]) + 12
                        pm = f"{str(eveConvert):02}:{firstNum[1]}"
                        listTime.append(pm)

                    if int(firstNum[1]) > 59:
                        raise ValueError
            else:
            # if single num
                singleDigit = i.split(" ")

                if "AM" in singleDigit[1]:
                    firstNum = int(singleDigit[0])
                    if firstNum == 12:
                        am = f"00:00"
                        listTime.append(am)
                    else:
                        am = f"{firstNum:02}:00"
                        listTime.append(am)

                if "PM" in singleDigit[1]:
                    firstNum = int(singleDigit[0])
                    if firstNum == 12:
                        pm = f"12:00"
                        listTime.append(pm)
                    else:
                        eveConvert = firstNum + 12
                        pm = f"{str(eveConvert):02}:00"
                        listTime.append(pm)

        return " to ".join(listTime)

    except:
        raise ValueError

if __name__ == "__main__":
    main()