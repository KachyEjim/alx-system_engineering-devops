#!/usr/bin/python3
"""
0-main
"""
import sys

import pdb


if __name__ == "__main__":
    number_of_subscribers = __import__("0-subs").number_of_subscribers
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        n = number_of_subscribers(sys.argv[1])
        print("{:d}".format(n))
