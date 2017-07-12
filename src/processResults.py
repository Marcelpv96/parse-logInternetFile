from parser import parseFile
import datetime
import matplotlib.pylab as plt
import json


class processResults():
    def __init__(self, results):
        self.results = parseFile.main(results)

    def biggerThanFivSec(self):
        accomulated = 0
        for seconds in self.results.cutsForSecond.values():
            if seconds > 5:
                accomulated += 1
        return str(accomulated)

    def totalTime(self):
        total = sum(self.results.cutsForSecond.values())
        return str(datetime.timedelta(seconds=total))

    def microCuts(self):
        accomulated = 0
        for seconds in self.results.cutsForSecond.values():
            if seconds == 1:
                accomulated += 1
        return str(accomulated)

    def biggestCut(self):
        allSecs = self.results.allCutsFormated
        maxim = max(allSecs.values())
        return allSecs.keys()[allSecs.values().index(maxim)] \
            + " amb duracio de " + \
            str(datetime.timedelta(seconds=maxim))

    def writeResultsAsJson(self):
        resultsFile = open(self.results.fileName + '_CutsForSecond', 'w+')
        json.dump(self.results.allCutsFormated, resultsFile)
        resultsFile.close()

    def plotData(self):
        lists = sorted(self.results.cutsForSecond.items())
        x, y = zip(*lists)
        plt.figure(figsize=(12, 9))
        plt.plot(x, y)
        plt.savefig(self.results.fileName + "_results.png")

    def summaryOfAllData(self):
        f = open(self.results.fileName + '_summary', 'w+')
        f.write("> MICRO TALLS 1 SEG: " + self.microCuts() + '\n')
        f.write("> TALLS DE MES 5 SEG: " + self.biggerThanFivSec() + '\n')
        f.write("> TEMPS TOTAL SENSE CONEXIO: " + self.totalTime() + '\n')
        f.write("> TALL MES LLARG, a les " + self.biggestCut() + '\n')
        f.close()
