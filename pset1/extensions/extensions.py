file = input("File name: ").strip().lower()



gif = file.endswith(".gif")
jpg = file.endswith(".jpg")
jpeg = file.endswith(".jpeg")
png = file.endswith(".png")
pdf = file.endswith(".pdf")
txt = file.endswith(".txt")
is_zip = file.endswith(".zip")

if gif:
    print("image/gif")
elif jpg or jpeg:
    print("image/jpeg")
elif png:
    print("image/png")
elif pdf:
    print("application/pdf")
elif txt:
    print("text/plain")
elif is_zip:
    print("application/zip")
else:
    print("application/octet-stream")
