#!/usr/bin/env python
# encoding=utf8
from __future__ import print_function

import sys


def main():
    """run command based on sys.argv[1]."""
    command = sys.argv[1]
    if not command in globals():
        sys.stderr.write("Invalid command: {}".format(command))
        sys.exit(1)
    globals()[command]()


if __name__ == '__main__':
    main()
