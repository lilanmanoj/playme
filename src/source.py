import mimetypes as MimeTypes
import xml.etree.ElementTree as ET
import urllib.parse as UrlParse
import os as OS
class Playlist:
    file = ""
    mimeType = ""
    output = []

    def __init__(self, file) -> None:
        self.file = file
    
    def process(self):
        self.mimeType = self.get_mime()
        playlistFileName = self.get_file_name_without_extension(self.file)

        print("Info: Start processing playlist..")

        if self.mimeType[0] == "application/xml":
            print("Info: xml playlist detected.")

            tree = ET.parse(self.file)
            root = tree.getroot()
            
            if root.tag == "rhythmdb-playlists":
                for playlist in root.findall('playlist'):
                    playlistTitle = playlist.get('name')
                    tracks = []
                    
                    for location in playlist.iter("location"):
                        path = self.get_path(location.text)
                        tracks.append(path)
                    
                    dictPlaylist = {
                        "title": playlistTitle,
                        "tracks": tracks
                    }

                    self.output.append(dictPlaylist)

        elif self.mimeType[0] == "application/xspf+xml":
            print("Info: xspf playlist detected.")

            tree = ET.parse(self.file)
            root = tree.getroot()
            playlistTitle = root.find("{http://xspf.org/ns/0/}title") or playlistFileName
            tracklist = root.find("{http://xspf.org/ns/0/}trackList")
            tracks = []

            for track in tracklist.findall("{http://xspf.org/ns/0/}track"):
                path = self.get_path(track.find("{http://xspf.org/ns/0/}location").text)
                tracks.append(path)
            
            dictPlaylist = {
                "title": playlistTitle,
                "tracks": tracks
            }
            
            self.output.append(dictPlaylist)
        
        else:
            # TO-DO: Other playlist processes ex: m3u
            print("Error: Unsupported filetype!")
        
        print("Info: Playlist process done.")

        return self.output

    def get_mime(self):
        return MimeTypes.guess_type(self.file)
    
    def get_path(self, url):
        sanitizedPath = UrlParse.unquote(url).replace("file:///", "/")
        return OS.fspath(sanitizedPath)

    def get_file_name_without_extension(self, file_path):
        return OS.path.splitext(OS.path.basename(file_path))[0]