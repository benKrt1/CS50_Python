import sys
import os
from PIL import Image, ImageOps

def main():
    check_file()
    try:
        image = Image.open(sys.argv[1])
        shirt = Image.open("shirt.png")
        photo = ImageOps.fit(image, shirt.size)
        photo.paste(shirt, (0, 0), shirt)
        photo.save(sys.argv[2])
        
    except FileNotFoundError:
        sys.exit("Input does not exist")

def check_file():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
        
    valid_extensions = (".jpg", ".jpeg", ".png")
    ext1 = os.path.splitext(sys.argv[1])[1].lower()
    ext2 = os.path.splitext(sys.argv[2])[1].lower()
    
    if not ext1.endswith(valid_extensions) or not ext2.endswith(valid_extensions):
        sys.exit("Invalid output")
    if ext1 != ext2:
        sys.exit("Input and output have different extensions")

if __name__ == "__main__":
    main()