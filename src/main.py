import argparse as ArgParse
import collections
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

print(collection)

# Initiate target destination
dest = Target.Destination(args.destination)
dest.write()