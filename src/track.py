import shutil as Shutil
import os.path as Path

class Media:
    track = ""

    def __init__(self, track) -> None:
        self.track = track

    def copy(self, destination):
        if Path.isfile(self.track):
            Shutil.copy(self.track, destination)