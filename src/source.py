import mimetypes as MimeTypes

class Playlist:
    file = ""
    mimeType = ""

    def __init__(self, file) -> None:
        self.file = file

    def identify(self):
        self.mimeType = MimeTypes.guess_type(self.file)
        return self.mimeType

    def read(self):
        print(self.file)