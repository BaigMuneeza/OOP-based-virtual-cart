##Manages list: instantiates an empty list, we can read any file that will be appeneded as a 2d list,we can save it in a .txt file

from FileReaderSaver import FileSaver
from FileReaderSaver import FileReader

class ListManager(list):
    def __init__(self,obj=[]):##instantiates an empty list
                self.general_list=obj
          

    def saveToFile(self, FileName):#saves in file
        fs=FileSaver()
        fs.saveToFile(self.general_list,FileName)

    def readFromFile(self, FileName):#reads from file
        fr=FileReader()
        fr.readFromFile(self.general_list,FileName)
    def __str__(self):
        strg=''
        for item in self.general_list:
            strg+=str(item[0])+', '+str(item[1])+', '+str(item[2])+', '+str(item[3])+'\n'
        return strg
    
    def printHistory(self,j):
         print()
         for i in j:
             if i==0:
                 pass
             else:
                print('ID :',i[0])
                print('Name Of Product: ',i[1])
                print('Price : Rs.',i[2])
                print('Quantity :',i[3])
                print()
