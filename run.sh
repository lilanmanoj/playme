#!/bin/sh

Help()
{
   # Display Help
   echo "Read media from playlist and copy to destination"
   echo
   echo "Syntax: run.sh [-h|--help] [-S] [-D]"
   echo "options:"
   echo "h|help   Help."
   echo "S        Source playlist file location"
   echo "D        Copy destination"
   echo
}

SOURCE=""
DESTINATION=""

while getopts ":hS:D:" option; do
   case $option in
        h) # display Help
            Help
            exit
            ;;
        
        S) # Fetch source
            SOURCE=$OPTARG
            ;;

        D) # Fetch destination
            DESTINATION=$OPTARG
            ;;

        \?) # Invalid option
            echo "Error: Invalid option"
            exit
            ;;
   esac
done

if [ -z "$SOURCE" ];
then
    read -p "Enter playlist source path: " SRC
    SOURCE=$(eval "echo $SRC")
fi

if [ -z "$DESTINATION" ];
then
    read -p "Enter copy destination path: " DES
    DESTINATION=$(eval "echo $DES")
fi

cd ./src
python3 main.py "$SOURCE" "$DESTINATION"