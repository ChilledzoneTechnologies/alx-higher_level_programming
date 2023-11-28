#!/usr/bin/python3

"""Print the alphabet in lowercase, not followed by a new line."""
for n in range(0, 26):
    print("{:s}".format(chr(ord('a') + n)), end="")
