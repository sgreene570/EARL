"""
earl.py
Email alias traversal program
Initial python hack out
"""


import argparse


def main():
    parser = argparse.ArgumentParser(description='Email Alias Lookup')
    parser.add_argument('file', type=str, nargs='+', help="Alias file name(s)")
    parser.add_argument('--alias', type=str, nargs='+', help="Alias to find")
    args = parser.parse_args()
    alias_dict = {}

    for f in args.file:
        alias_list = open(f, 'r')
        for line in alias_list:
            if "#" == line[0] or ":" not in line:
                continue
            alias = line[:line.index(":")].strip()
            name = line[line.index(":") + 1:].strip()
            if alias in args.alias:
                if alias in alias_dict.keys():
                    alias_set = alias_dict[alias]
                    alias_set.add(name)
                    alias_dict[alias] = alias_set
                else:
                    alias_dict[alias] = {name}

    for alias in args.alias:
        print(alias + ": " + 
            str(alias_dict[alias]).replace("'", "").strip("{}'"))


if __name__ =="__main__":
    main()
