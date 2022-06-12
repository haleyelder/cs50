# 1 Um,
# 1 um..
# 1 um?
# 1 Um, thanks for the album.
# 2 Um, thanks, um...
#--------------------------#
# yummy
# instrument
# aluminum
# album.

import re

def main():
    print(count(input("Text: ")))

def count(s):
    return len(re.findall(r"\b(um)|(Um)|('...')", s))


if __name__ == "__main__":
    main()