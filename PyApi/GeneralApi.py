import json
import os




class FileManager:

    def __init__(self, path, filetype):
        self.path = path
        self.filetype = filetype



    # Returns the contents of the file sent to the class
    def getFileContents(self):
        path = self.path
        filetype = self.filetype

        if filetype == None:
            with open(path, 'r') as file:
                fileData = file.read()

                return fileData

        elif filetype == 'json':
            with open(path, 'r') as json_file:
                json_data = json.load(json_file)

                return json_data

        else:
            raise Exception(filetype + ' not supported u stoopid man')



    # Replaces the old contents of the file with the new ones
    def writeToFile(self, data):
        path = self.path
        filetype = self.filetype

        if filetype == None:
            with open(path, 'w') as file:
                file.write(data)

        elif filetype == 'json':
            with open(path, 'w') as json_file:
                json_file.dump(data)

        else:
            raise Exception(filetype + ' not supported u stoopid man')



    # TODO
    def appendToFile(self, data):

        pass




class StringManager:

    # Returns a string with all non alphabet chracters removed
    def filterAlpha(string):
        filteredString = ''.join(i for i in str(string) if i.isalpha())
        return filteredString



    # Returns a string with all non numeric chracters removed
    def filterNum(string):
        filteredString = ''.join(i for i in str(string) if i.isdigit())
        return filteredString



    # Returns a string with all non alphanumerical characters removed
    def filterAlphaNum(string):
        filteredString = ''.join(i for i in str(string) if i.isalnum())
        return filteredString




class ListManager:

    # Returns a list with all the contents of the sent lists
    def combineLists(lists = []):
        combinedList = []

        for uncombinedList in lists:
            for item in uncombinedList:
                combinedList.append(item)


        return combinedList
