import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    # extract URL with src
    URL = re.search(r'src=[\'"]([^\'"]+)', s)
    if URL:
        URL = URL.group(1)
        youtubeLink = re.search(r'(youtube)', URL)
        if youtubeLink:
        #     # extract youtube ID
            ytID = re.sub(r"^(https?://)?(www\.)?youtube\.com/([a-z0-9_]+)", "", URL)
            return f"https://youtu.be{ytID}"
        else:
            return None


if __name__ == "__main__":
    main()