import os.path as Path
import os as Os
class Destination:
    dir = ""

    def __init__(self, dir) -> None:
        self.dir = dir
    
    def check(self):
        return Path.exists(self.dir) and Path.isdir(self.dir)

    def create(self, newFolder = ""):
        path = self.dir

        if newFolder != "":
            path = path + "/" + self.sanitize(newFolder)

        Os.mkdir(path)
        return path
    
    def sanitize(self, dirName):
        return dirName.replace("/", " ")