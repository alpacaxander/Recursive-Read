#!/usr/bin/env python3

import argparse
import os

def read(data, keys):
    if len(keys) == 0:
        return data
    if (type(data) is list):
        keys[0] = int(keys[0])
    return read(data[keys[0]], keys[1:])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=str,
        help='Input file name')
    parser.add_argument('-k', '--keys', nargs='+',
        help='Keys in order of first layer to last')

    args = parser.parse_args()

    s = open(args.input, 'r').read()
    data = eval(s)
    try:
        print(read(data, args.keys))
    except KeyboardInterrupt:
        raise
    except:
        return

if __name__ == "__main__":
    main()
