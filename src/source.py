import mimetypes as MimeTypes
import xml.etree.ElementTree as ET
class Playlist:
    file = ""
    mimeType = ""

    def __init__(self, file) -> None:
        self.file = file
    
    def process(self):
        self.mimeType = self.get_mime()
        
        if self.mimeType == "application/xml":
            tree = ET.parse(self.file)
            root = tree.getroot()

            for playlist in root.findall('playlist'):
                playlistTitle = playlist.find('title') or playlist.get('name')
                print(playlistTitle)

    def get_mime(self):
        return MimeTypes.guess_type(self.file)

    def read(self):
        print(self.file)