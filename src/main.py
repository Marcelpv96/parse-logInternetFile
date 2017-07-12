#!/usr/bin/env python
import sys
from parser import parseFile
from processResults import processResults
if __name__ == "__main__":
    try:
        fileName = sys.argv[1]
        newFile = fileName.replace(".txt", "")
        pars = parseFile(fileName)
    except IndexError:
        print "Error en el nom de fitxer"
        sys.exit(-1)
    except IOError:
        print "Error en el nom de fitxer"
        sys.exit(-1)
    results = processResults(pars)
    results.plotData()
    results.summaryOfAllData()
