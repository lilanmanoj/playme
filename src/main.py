import argparse as ArgParse
import track as Track
import source as Source
import target as Target

# Read arguments
parser = ArgParse.ArgumentParser(
    prog='main',
    description='Read media from playlist and copy to destination')
parser.add_argument('source')
parser.add_argument('destination')
args = parser.parse_args()

# Initiate playlist
plst = Source.Playlist(args.source)
collection = plst.process()

for playlist in collection:
    title = playlist['title']
    tracks = playlist['tracks']

    # Initiate target destination
    dest = Target.Destination(args.destination)
    
    if dest.check() is not True:
        dest.create()
    
    path = dest.create(title)
    
    for track in tracks:
        media = Track.Media(track)
        media.copy(path)