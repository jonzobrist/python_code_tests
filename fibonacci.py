#!env python
"""Simple fibonacci sequence in Python"""

import argparse


def main(start=1, maximum=144):
    """
    Main function, if this were a library,
    it'd be called fibonacci
    """
    last = start  # Fibonacci sequence repeats first numbers!
    while start <= maximum:  # How we know when to stop
        print start  # Our actual output
        start, last = last, start + last  # Increment the sequence, 2 for 1


def greater_than_one(value):
    """
    Given integer of 'value'
    if it's > 0, it's ok
    otherwise, raise an exception
    """
    int_value = int(value)
    if int_value < 1:
        raise argparse.ArgumentTypeError("%s is less than 1" % value)
    return int_value

if __name__ == "__main__":
    # If this was run as a script, setup args and call main()
    PARSER = argparse.ArgumentParser(
        description="Prints fibonacci from start to end")
    PARSER.add_argument(
        "--start", required=False, default=1,
        action='store', dest='start', type=greater_than_one)
    PARSER.add_argument(
        "--max", required=False, default=144,
        action='store', dest='maximum', type=greater_than_one)
    ARGS = PARSER.parse_args()
    if ARGS.start >= ARGS.maximum:
        raise argparse.ArgumentTypeError(
            "Max %s is less than start %s" % (ARGS.maximum, ARGS.start))
main(start=ARGS.start, maximum=ARGS.maximum)
