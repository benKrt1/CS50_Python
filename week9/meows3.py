'''import sys

if len(sys.argv) == 1:
    print("meow")
elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    n = int(sys.argv[2])
    for _ in range(n):
        print("meow")
else:
    print("usage: meows.py")
'''

import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help="number of time to meow", type=int)
#to meows3.py otan to trexis perni sto terminal argument kai kanis 
#import to argparse to argparse.ArgumentParser(description="Meow like a cat")
# einai gia otan o xristis patisi python meows.py -h/--help na tou
# diksi ti kani to -n kai gia poio logo einai
# to  parser.add_argument("-n", default=1, help="number of time to meow", type=int)
# einai gia na valis extra argoument opos to "-n" (to numero pou tha kani "meow") 
# to default=1 einai gia to "-n" oti den einai ipoxreotiko 
# to help="number of time to meow" einai otan o xristis patai -h/--help ti na tou vgali stin perigrafi
# kai to type=int einai gia to ti idous tha einai to argument pou tha vali o xristis
args = parser.parse_args()


for _ in range(int(args.n)):
    print("meow")