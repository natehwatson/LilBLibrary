#!/bin/bash

COMMAND=$1
shift

PYTHONPATH="/Users/natewatson/Documents/forFun"

case "$COMMAND" in
    ls)
        PYTHONPATH="$PYTHONPATH" python3 -c "import lilBLibrary; lilBLibrary.importLibrary(); lilBLibrary.printDict()"
        ;;
    search)
        STRING="$1"
        RETURN_LENGTH="$2"
        if [[ "$2" =~ ^[0-9]+$ ]]; then
            RETURN_LENGTH="$2"
        else
            RETURN_LENGTH=3
        fi
        PYTHONPATH="$PYTHONPATH" python3 -c "import lilBLibrary; lilBLibrary.importLibrary(); lilBLibrary.searchLyric(\"$STRING\", $RETURN_LENGTH);"
        ;;
    searchSong)
        SONG_TITLE="$1"
        RETURN_LENGTH="$2"
        if [[ "$2" =~ ^[0-9]+$ ]]; then
            RETURN_LENGTH="$2"
        else
            RETURN_LENGTH=3
        fi
        PYTHONPATH="$PYTHONPATH" python3 -c "import lilBLibrary; lilBLibrary.importLibrary(); lilBLibrary.searchSong(\"$SONG_TITLE\", $RETURN_LENGTH);"
        ;;
    searchNotes)
        STRING="$1"
        RETURN_LENGTH="$2"
        if [[ "$2" =~ ^[0-9]+$ ]]; then
            RETURN_LENGTH="$2"
        else
            RETURN_LENGTH=3
        fi
        PYTHONPATH="$PYTHONPATH" python3 -c "import lilBLibrary; lilBLibrary.importLibrary(); lilBLibrary.searchNotes(\"$STRING\", $RETURN_LENGTH);"
        ;;
    addSong)
        SONG_TITLE="$1"
        LYRICS="$2"
        PYTHONPATH="$PYTHONPATH" python3 -c "import lilBLibrary; lilBLibrary.importLibrary(); lilBLibrary.addSong(\"$SONG_TITLE\", \"$LYRICS\"); lilBLibrary.exportLibrary();"
        ;;
    editSong)
        OLD_SONG_TITLE="$1"
        OLD_SONG_LYRICS="$2"
        NEW_LYRICS="$3"
        NEW_SONG_TITLE="$4"
        if [[ -z "$NEW_SONG_TITLE" ]]; then
            NEW_SONG_TITLE="$OLD_SONG_TITLE"
        fi
        PYTHONPATH="$PYTHONPATH" python3 -c "import lilBLibrary; lilBLibrary.importLibrary(); lilBLibrary.editSong(\"$OLD_SONG_TITLE\", \"$OLD_SONG_LYRIC\", \"$NEW_LYRICS\", \"$NEW_SONG_TITLE\"); lilBLibrary.exportLibrary();"
        ;;
    deleteSong) 
        SONG_TITLE="$1"
        PYTHONPATH="$PYTHONPATH" python3 -c "import lilBLibrary; lilBLibrary.importLibrary(); lilBLibrary.deleteSong(\"$SONG_TITLE\"); lilBLibrary.exportLibrary();"
        ;;
    deleteLyric)
        SONG_TITLE="$1"
        LYRIC="$2"
        PYTHONPATH="$PYTHONPATH" python3 -c "import lilBLibrary; lilBLibrary.importLibrary(); lilBLibrary.deleteLyric(\"$SONG_TITLE\", \"$LYRIC\"); lilBLibrary.exportLibrary();"
        ;;
    addNote)
        SONG_TITLE="$1"
        NOTE="$2"
        PYTHONPATH="$PYTHONPATH" python3 -c "import lilBLibrary; lilBLibrary.importLibrary(); lilBLibrary.addNotes(\"$SONG_TITLE\", \"$NOTE\"); lilBLibrary.exportLibrary();"
        ;;
    editNote)
        SONG_TITLE="$1"
        OLD_NOTE="$2"
        NEW_NOTE="$3"
        PYTHONPATH="$PYTHONPATH" python3 -c "import lilBLibrary; lilBLibrary.importLibrary(); lilBLibrary.editNotes(\"$SONG_TITLE\", \"$OLD_NOTE\", \"$NEW_NOTE\"); lilBLibrary.exportLibrary();"
        ;;
    deleteNote)
        SONG_TITLE="$1"
        NOTE="$2"
        PYTHONPATH="$PYTHONPATH" python3 -c "import lilBLibrary; lilBLibrary.importLibrary(); lilBLibrary.deleteNote(\"$SONG_TITLE\", \"$NOTE\); lilBLibrary.exportLibrary();"
        ;;
    *)
        echo "Usage: ls: List all songs and associated lyrics"
        echo "       search <string> <int>: Search for a string in the lyrics. Returns <int> number of results (default 3)"
        echo "       searchSong <song title> <int>: Search for a song by title. Returns <int> number of results (default 3)"
        echo "       searchNotes <string> <int>: Search for a string in the notes. Returns <int> number of results (default 3)"
        echo "       addSong <song title> <lyrics>: Add a new song with lyrics"
        echo "       editSong <old song title> <old lyrics> <new lyrics> <new song title>: Edit an existing song's lyrics"
        echo "       deleteSong <song title>: Delete a song"
        echo "       deleteLyric <song title> <lyric>: Delete a lyric from a song"
        echo "       addNote <song title> <note>: Add a note to an existing song"
        echo "       editNote <song title> <old note> <new note>: Edit an existing note for a song"
        echo "       deleteNote <song title> <note>: Delete a note from a song"
        exit 1
        ;;
esac