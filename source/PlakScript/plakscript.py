class PlakScript:
    def __init__(self,url) -> None:
        
        self.FilePath = url
        pass

    def read(self):
        
        with open(self.FilePath) as f:
            file = f.read()
            if(file.replace(" ","") == ""):
                return [],[]
            musics = file.split(",")
            originalNames = []
            unicodedNames = []
            for item in musics:
                names = item.split("|=|")

                originalNames.append(names[0])
                unicodedNames.append(names[1])

            return originalNames,unicodedNames

            pass
        pass

    def write(self,originalName,unicodedName):
        originalNames , unicodedNames = self.read()
        originalNames.append(originalName)
        unicodedNames.append(unicodedName)

        fileString = ""

        index = 0
        for item in originalNames:
            fileString += (originalNames[index] + "|=|" + unicodedNames[index])
            if index+1 != len(originalNames):
                fileString += ","
            index+= 1
            pass

        with open(self.FilePath,"w") as f:
            f.write(fileString)
            pass
        pass

    def delete(self,index):
        originalNames , unicodedNames = self.read()
        originalNames.pop(index)
        unicodedNames.pop(index)

        fileString = ""

        index = 0
        for item in originalNames:
            fileString += (originalNames[index] + "|=|" + unicodedNames[index])
            if index+1 != len(originalNames):
                fileString += ","
            index+= 1
            pass

        with open(self.FilePath,"w") as f:
            f.write(fileString)
            pass
        pass