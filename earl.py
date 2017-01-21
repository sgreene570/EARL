"""
earl.py
Email alias traversal program
Initial python hack out
"""


import argparse


def main():
    parser = argparse.ArgumentParser(description='Email Alias Lookup')
    parser.add_argument('file', type=str, nargs='+', help="Alias file name(s)")
    parser.add_argument('--alias', type=str, nargs='+', help="Alias to be found")
    args = parser.parse_args()
    alias_dict = {}

    for f in args.file:
        for line in f:
            alias = line[:line.index(":")]
            name = line[line.index(":") + 1:]
            if alias in alias_dict.keys():

 


if __name__ =="__main__":
    main()
