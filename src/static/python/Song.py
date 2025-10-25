class Song:
    def __init__(self, title, lyrics="", album=""):
        self.title = title
        self.album = album
        self.lyrics = lyrics

    def __str__(self):
        return self.title, self.album, self.lyrics

    def __eq__(self, other):
        return self.title == other.title and self.album == other.album
    
def setLyrics(self, lyrics):
    self.lyrics = lyrics

def getLyrics(self):
    return self.lyrics

def setTitle(self, title):
    self.title = title

def getTitle(self):
    return self.title

def setAlbum(self, album):
    self.album = album

def getAlbum(self):
    return self.album




