import argparse as ArgParse
import source as Source
import target as Target

parser = ArgParse.ArgumentParser(
    prog='main',
    description='Read media from playlist and copy to destination')
parser.add_argument('source')
parser.add_argument('destination')
args = parser.parse_args()

plst = Source.Playlist(args.source)
plstMimeType = plst.identify()

dest = Target.Destination(args.destination)
dest.write()