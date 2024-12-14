'''#Say Ver 1.0
import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.pig("hello, " + sys.argv[1])'''

#Say Ver 2.0
import sys
import sayings

if len(sys.argv) == 2:
    sayings.hello(sys.argv[1])
