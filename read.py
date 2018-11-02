#!/usr/bin/env python3

import argparse
import os

def read(data, keys):
    """Search through data with given keys

    read(data, [a,b,c]) is equivilent to
    data[a][b][c]
    If the current level is a list then it
        tries to convert key to int
    """
    if len(keys) == 0:
        return data
    if (type(data) is list):
        keys[0] = int(keys[0])
    return read(data[keys[0]], keys[1:])

def extractData(filename)
    """Read a dictionary/list from file"""
    s = open(filename, 'r').read()
    data = eval(s)
    return data

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=str,
        help='Input file name')
    parser.add_argument('-k', '--keys', nargs='+',
        help='Keys in order of first layer to last')

    args = parser.parse_args()

    try:
        data = extractData(args.input)
        print(read(data, args.keys))
    except KeyboardInterrupt:
        raise
    except:
        return

if __name__ == "__main__":
    main()
