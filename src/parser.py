def format(second):
    x = str(second)
    return x[:-4] + ':' + x[-4:-2] + ':' + x[-2:]


class parseFile():
    def __init__(self, file):
        self.fileName = file.replace(".txt", "")
        self.file = open(file)
        self.seconds = []
        self.cutsForSecond = {}
        self.allCutsFormated = {}

    def processLines(self):
        self.seconds = [int(line.split()[3].replace(":", ""))
                        for line in self.file]

    def countSeconds(self):
        lastSecond = self.seconds[0]
        self.cutsForSecond[lastSecond] = 1
        dif = 1
        for second in self.seconds:
            if second - lastSecond == dif:
                dif += 1
                self.cutsForSecond[lastSecond] += 1
            else:
                dif = 1
                self.cutsForSecond[second] = 1
                lastSecond = second

    def formatAllKeys(self):
        self.allCutsFormated = {format(second): self.cutsForSecond[second]
                                for second in self.cutsForSecond.keys()}

    @staticmethod
    def main(obj):
        obj.processLines()
        obj.countSeconds()
        obj.formatAllKeys()
        return obj
