#! /usr/bin/env python
"""Testing sys.exit."""

import sys


def main():
    """Does nothing important."""

    if len(sys.argv) < 2:
        sys.exit('The arguments were not enough')
    print('{} is very awesome'.format(sys.argv[1]))


if __name__ == '__main__':
    sys.exit(main())
