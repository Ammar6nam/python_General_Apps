from abc import ABC,abstractmethod
    
class files:
    def __init__(self,fileName='') -> None:
        self.fileName=fileName
        self.getFileType()    
    
    def getFileType(self):
        print(f'file type is txt')

    def read (self):
        print('read File')

    def write (self,data={}):
        print('wrote file')

    def update (self,data):
        print('updated file')

    def close(self):
        print('closed File')


class files(ABC):
    def __init__(self,fileName='') -> None:
        self.fileName=fileName
        #self.getFileType()    
    
    @abstractmethod
    def getFileType(self):
        print(f'file type is txt')


    @abstractmethod
    def read (self):
        print('read File')

    def write (self,data={}):
        print('wrote file')

    def update (self,data):
        print('updated file')

    def close(self):
        print('closed File')


class jsonFile(files):
    def getFileType(self):
        #return super().getFileType()
        print(f'File type is json')

    def read(self):
        #return super().read()
        print('Reading CSV file')

    def save(self):
        pass

class csvFile(files):
    def getFileType(self):
        #return super().getFileType()
        print(f'File type is CSV')

    def read(self):
        #return super().read()
        print('Reading CSV file')

# newJsonFile=jsonFile('Shop_data.json')
# newCsvFile=csvFile('data.csv')
# shopInformation=csvFile('shopData.csv')

# # listOfFileWorker=[newJsonFile,newCsvFile,shopInformation]
# # for file in listOfFileWorker:
# #     file.read()

# class utility:
#     def display (self,fileClass):
#         fileClass.read()
#         print(fileClass.fileName)

# help=utility()
# help.display(newJsonFile)
def fileClassFactory (fileName):
    if fileName.endswith('.csv'):
        fileObject=csvFile()
    elif fileName.endswith('.json'):
        fileObject=jsonFile(fileName)
        return fileObject




listOfFiles=['a.csv','b.csv','c.json','d.csv','e.json']
for fileName in listOfFiles:
    if fileName.endswith('.csv'):
        fileObject=csvFile()
    elif fileName.endswith('.json'):
        fileObject.read()
        fileObject.save()


