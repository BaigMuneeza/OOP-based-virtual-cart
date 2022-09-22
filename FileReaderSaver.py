class FileSaver:###saves obj in files
    def saveToFile(self,obj,fileName):
        f=open(fileName,'w')
        for item in obj:
            f.write(str(item)+'\n')
        f.close()

class FileReader:###reads from file and appends in obj.
    def readFromFile(self,obj,fileName):
        f=open(fileName,'r')
        for line in f:
            obj.append(eval(line))
        f.close()
