
from .Song import Song

def createSong(title, lyrics, album=""):
    return Song(title, lyrics, album)