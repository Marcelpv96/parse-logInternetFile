#!/usr/bin/env python
import sys
if __name__ == "__main__":
    try:
        pars = parseFile(sys.argv[1])
    except IndexError:
        print "Error: falta nom de fitxer"
        sys.exit(-1)
    results = processResults(pars)
    results.summaryOfAllData()
