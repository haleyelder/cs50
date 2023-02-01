# need to add test cases; test_numb3rs.py -- 2 or more functions to test
# True: xxx.xxx.xxx.xxx - min 1 num, max 3 nums per period
# True: 0 - 255 range only
# False: "cat"

import re

def main():
    print(validate(input("IPV4 Address: ").strip()))

# return True/False validation
def validate(ip):
    ipLength = ip.split('.')
    if len(ipLength) > 4 or len(ipLength) <= 3:
        return False
    else:
        ipCheck = "^(([0-1]?[0-9]?[0-9]?|2[0-4][0-9]|25[0-5])\\.){3}([0-1]?[0-9]?[0-9]?|2[0-4][0-9]|25[0-5]){1}$"
        if (re.search(ipCheck, ip)):
            return True
        else:
            return False


if __name__ == "__main__":
    main()