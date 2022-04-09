import imp
import mimetypes as MimeTypes
import xml.etree.ElementTree as ET
import xml.dom as Dom
class Playlist:
    file = ""
    mimeType = ""

    def __init__(self, file) -> None:
        self.file = file
    
    def process(self):
        self.mimeType = self.get_mime()

        if self.mimeType[0] == "application/xml":
            tree = ET.parse(self.file)
            root = tree.getroot()

            if root.tag == "rhythmdb-playlists":
                for playlist in root.findall('playlist'):
                    playlistTitle = playlist.get('name')
                    
                    for location in playlist.iter("location"):
                        print(location.text)

        elif self.mimeType[0] == "application/xspf+xml":
            tree = ET.parse(self.file)
            root = tree.getroot()
            playlistTitle = root.find("{http://xspf.org/ns/0/}title").text
            tracklist = root.find("{http://xspf.org/ns/0/}trackList")

            for track in tracklist.findall("{http://xspf.org/ns/0/}track"):
                print(track.find("{http://xspf.org/ns/0/}location").text)

    def get_mime(self):
        return MimeTypes.guess_type(self.file)

    def read(self):
        print(self.file)