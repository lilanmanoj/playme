import argparse as ArgParse
import track as Track
import source as Source
import target as Target
import click as Click

def display_ascii_art():
    print('\n')
    print('''
    (  _ \(  )    /__\ ( \/ )(  \/  )( ___)
    )___\/ )(__  /(__)\ \  /  )    (  )__) 
    (__)  (____)(__)(__)(__) (_\/\/\_)(____)
    ''')
    print('\n')

def main(source, destination):
    # Initiate playlist
    plst = Source.Playlist(source)
    collection = plst.process()

    for playlist in collection:
        title = playlist['title']
        tracks = playlist['tracks']

        # Initiate target destination
        dest = Target.Destination(destination)
        
        print("Info: Checking destination..")

        if dest.check() is not True:
            print("Info: Destination not available!")
            dest.create()
        
        confirmed = Click.confirm("Confirm copy tracks for playlist \"" + title + "\"", True)
        
        if confirmed:
            path = dest.create(title)

            print("Info: Copying tracks for " + title + " ...")

            for track in tracks:
                media = Track.Media(track)
                media.copy(path)
            
            print("Info: Track copy done!\n")
        else:
            print("Info: Skipping copy tracks for " + title + " ...")
    
    print("Quiting program!")

# Read arguments
parser = ArgParse.ArgumentParser(
    prog='main',
    description='Read media from playlist and copy to destination')
parser.add_argument('source')
parser.add_argument('destination')
args = parser.parse_args()

display_ascii_art()
main(args.source, args.destination)