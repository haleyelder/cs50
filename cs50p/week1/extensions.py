# TEST CASES
# - happy.jpg >> image/jpeg
# - document.pdf >> application/pdf

# .gif > image/gif
# .jpg > image/jpeg
# .jpeg > image/jpeg
# .png > image/png
# .pdf > application/pdf
# .txt > text/plain
# .zip > application/zip
# - default output >  application/octet-stream

text = input("File name: ")
# find period
text = text.split('.')
# var for last item, lowercase, no spaces
extension = text[-1].lower().strip()

if extension == "gif":
    print("image/gif")
elif extension == "jpg":
    print("image/jpeg")
elif extension == "jpeg":
    print("image/jpeg")
elif extension == "png":
    print("image/png")
elif extension == "pdf":
    print("application/pdf")
elif extension == "txt":
    print("text/plain")
elif extension == "zip":
    print("application/zip")
else:
    print("application/octet-stream")
