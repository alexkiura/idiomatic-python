#! /usr/bin/env python
# """Testing sys.exit."""

import sys


# def main():
#     """Does nothing important."""

#     if len(sys.argv) < 2:
#         sys.exit('The arguments were not enough')
#     print('{} is very awesome'.format(sys.argv[1]))


# if __name__ == '__main__':
#     sys.exit(main())

## Testing argument parsing
if __name__ == '__main__':
    try:
        print(open(sys.argv[1]).read())
    except IndexError:
        print('You forgot the file name:')
# import argparse

# if __name__ == '__main__.py':
#     parser = argparse.ArgumentParser(usage='main.py <filename>')
#     parser.add_argument('filename', help='The name of the file to use')
#     parsed = parser.parse_args(sys.argv)
#     print(open(parsed['filename']).read())