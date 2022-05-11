# missed one case, needs refactoring


# TEST CASES
# xx - CS50 >> Valid
# - CS05 >> Invalid
# xx - PI3.14 >> Invalid
# xx - H >> Invalid
# xx - OUTATIME >> Invalid

# REQUIREMENTS:
#  xx - start with 2 letters
#  xx - max 6 chars (letter/num) - min 2 chars
#   - numbers cannot be solely in the middle
#         eg: AAA222 yes, AAA22A no
#  xx - cannot start with 0
#  xx - no periods, spaces or punct
#     - to uppercase?


def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    length = len(s)

    # max 6, min 2 chars
    if length >= 2 and length <= 6:
        for letters in s:
            # break if not alpha or num (punct, space, etc case)
            if not s.isalnum():
                break

            #  first 2 char are letters
            if s[0:2].isalpha():
                # middle part of entry
                middle = s[1:-1]
                if middle.isnumeric() and middle.find(0):
                    break

                # true if ends with digit
                if s[-2].isdigit() and s[-1].isalpha():
                    break
                elif s[-2].isdigit():
                    return True
                elif s.isalpha():
                    return True

    else:
        return False

main()