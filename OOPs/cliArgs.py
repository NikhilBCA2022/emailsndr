import argparse as argparser    
import sys

# name=sys.argv[1]
# print(f"Hello {name}")

parser = argparser.ArgumentParser(description="User data")
parser.add_argument("name", help="Name of the user")
parser.add_argument("--age", help="Age of the user", type=int)

args = parser.parse_args()

print(f"Your name is {args.name} and your age is {args.age}")
