#!/usr/bin/env python

for i in xrange(100):
    output = "{} ".format(i)
    if i % 3 == 0:
        output = output + "Fizz"
    if i % 5 == 0:
        output = output + "Buzz"
    print output
