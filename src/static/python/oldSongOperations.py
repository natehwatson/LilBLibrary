from collections import defaultdict
import json

LIBRARY_PATH = "/Users/natewatson/Documents/forFun/library.json"

## colors
RESET = "\033[0m"
CYAN = "\033[36m"
GREEN = "\033[32m"
PURPLE = "\033[35m"
YELLOW = "\033[33m"


songToLyric = defaultdict(list) 
LyricToSong = defaultdict(list)
LyricToToken = defaultdict(list)
SongToToken = defaultdict(list)
SongToNotes = defaultdict(list)
SongToNotesTokens = defaultdict(list)
SongtoObject = []

def tokenize(lyric):
  tokenList = []
  tokens = lyric.split()
  for token in tokens:
    tokenList.append(token)
  return tokenList

def checkForExistingEntry(song, lyric):
  if song in songToLyric and lyric in songToLyric[song]:
    return True
  if lyric in LyricToSong and song in LyricToSong[lyric]:
    return True
  return False

def normalizeEntry(string):
  invalidChars = ["'", '"', "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "{", "}", "[", "]", "|", "\\", ";", ":", ",", ".", "<", ">", "/", "?"]
  result = string.lower()
  for char in invalidChars:
    result = result.replace(char, "")
  return result

def addSong(song, lyric):
  song = normalizeEntry(song)
  lyric = normalizeEntry(lyric)
  if checkForExistingEntry(song, lyric):
    print("This song already exists in the library.")
    return
  songToLyric[song].append(lyric)
  LyricToSong[lyric].append(song)
  print("Song added successfully.")

def editSong(oldSong, oldLyric, newLyric, newSong=None):
  if newSong is None:
    newSong = oldSong
  oldSong = normalizeEntry(oldSong)
  oldLyric = normalizeEntry(oldLyric)
  newSong = normalizeEntry(newSong)
  newLyric = normalizeEntry(newLyric)
  if oldSong in songToLyric and oldLyric in songToLyric[oldSong]:
    songToLyric[oldSong].remove(oldLyric)
    if not songToLyric[oldSong]:
      del songToLyric[oldSong]
    LyricToSong[oldLyric].remove(oldSong)
    if not LyricToSong[oldLyric]:
      del LyricToSong[oldLyric]
    songToLyric[newSong].append(newLyric)
    LyricToSong[newLyric].append(newSong)
    print("Song updated successfully.")
  else:
    print("Old song or lyric not found.")

def deleteSong(song):
  song = normalizeEntry(song)
  if song in songToLyric:
    for lyric in songToLyric[song]:
      LyricToSong[lyric].remove(song)
      if not LyricToSong[lyric]:
        del LyricToSong[lyric]
    del songToLyric[song]
    if song in SongToNotes:
      del SongToNotes[song]
    print("Song deleted successfully.")
  else:
    print("Song not found.")

def deleteLyric(song, lyric):
  song = normalizeEntry(song)
  lyric = normalizeEntry(lyric)
  if song in songToLyric and lyric in songToLyric[song]:
    songToLyric[song].remove(lyric)
    if not songToLyric[song]:
      del songToLyric[song]
      del SongToNotes[song]
    LyricToSong[lyric].remove(song)
    if not LyricToSong[lyric]:
      del LyricToSong[lyric]
    print("Lyric deleted successfully.")
  else:
    print("Song or lyric not found.")

def addNotes(song, note):
  song = normalizeEntry(song)
  note = normalizeEntry(note)
  SongToNotes[song].append(note)
  print("Note added successfully.")

def editNotes(song, oldNote, newNote):
  song = normalizeEntry(song)
  oldNote = normalizeEntry(oldNote)
  newNote = normalizeEntry(newNote)
  if song in SongToNotes and oldNote in SongToNotes[song]:
    SongToNotes[song].remove(oldNote)
    SongToNotes[song].append(newNote)
    print("Notes updated successfully.")
  else:
    print("Song or note not found.")

def deleteNote(song, note):
  song = normalizeEntry(song)
  note = normalizeEntry(note)
  if song in SongToNotes and note in SongToNotes[song]:
    SongToNotes[song].remove(note)
    if not SongToNotes[song]:
      del SongToNotes[song]
    print("Note deleted successfully.")
  else:
    print("Song or note not found.")

def printDict():
  sortedSongs = sorted(songToLyric.keys())
  num = 1
  for song in sortedSongs:
    print(f"{num}: {CYAN}{song}:{RESET} Notes: {SongToNotes[song]} {GREEN}Lyrics: {songToLyric[song]}{RESET}")
    num += 1

def searchSong(song, returnLength=3):
  pointsPerSong = defaultdict(int)
  song = normalizeEntry(song)
  searchTokens = tokenize(song)
  points = 0
  for song, dictTokens in SongToToken.items():
    for searchToken in searchTokens:
      if searchToken in dictTokens:
        pointsPerSong[song] += 1
        points += 1
  if points == 0:
    print("no matching songs found")
    return
  
  pointsPerSong = sorted(pointsPerSong.items(), key=lambda item: item[1], reverse=True)
  for song, points in pointsPerSong[0:returnLength]:
    print(f"Song: {CYAN}\'{song}\'{RESET} found with ", end = "")
    if SongToNotes[song]:
      print(f"notes: {SongToNotes[song]} and ", end = "")
    print(f"lyrics: {GREEN}{songToLyric[song]}{RESET}")
    returnLength -= 1
  if (returnLength > 0):
    print(f"no more results found.")

def searchLyric(string, returnLength=3):
  pointsPerLyric = defaultdict(int)
  string = normalizeEntry(string)
  searchTokenList = tokenize(string)
  points = 0
  for lyric, dictTokenList in LyricToToken.items():
    for token in searchTokenList:
      if token in dictTokenList:
        pointsPerLyric[lyric] += 1
        points += 1
  if points == 0:
    print("no matching lyrics found")
    return
  
  pointsPerLyric = sorted(pointsPerLyric.items(), key=lambda item: item[1], reverse=True)

  for lyric, points in pointsPerLyric[0:returnLength]:
    print(f"Lyric: {GREEN}\'{lyric}\'{RESET} found in: {CYAN}{LyricToSong.get(lyric)}{RESET}")
    returnLength -= 1
  if (returnLength > 0):
    print(f"no more results found.")

def searchNotes(string, returnLength=3):
  pointsPerSong = defaultdict(int)
  string = normalizeEntry(string)
  searchTokenList = tokenize(string)
  points = 0
  for song, dictTokenList in SongToNotesTokens.items():
    for token in searchTokenList:
      if token in dictTokenList:
        pointsPerSong[song] += 1
        points += 1
  if points == 0:
    print("no matching notes found")
    return
  
  pointsPerSong = sorted(pointsPerSong.items(), key=lambda item: item[1], reverse=True)

  for song, points in pointsPerSong[0:returnLength]:
    print(f"Notes: \'{SongToNotes[song]}\' about: {CYAN}{song}{RESET}")
    returnLength -= 1
  if (returnLength > 0):
    print(f"no more results found.")

def exportLibrary():
  with open(LIBRARY_PATH, "w") as f:
    json.dump({
      "songToLyric": songToLyric,
      "LyricToSong": LyricToSong,
      "SongToNotes": SongToNotes}, f)

def importLibrary():
  try:
    with open(LIBRARY_PATH, "r") as f:
      data = json.load(f)
      songToLyric.update(data["songToLyric"])
      LyricToSong.update(data["LyricToSong"])
      SongToNotes.update(data["SongToNotes"])
    for song in songToLyric:
      SongToToken[song] = tokenize(song)
    for lyric in LyricToSong:
      LyricToToken[lyric] = tokenize(lyric)
    for song, noteList in SongToNotes.items():
      for note in noteList:
        SongToNotesTokens[song] = tokenize(note)
    
  except FileNotFoundError:
    print("Library file not found. Starting with an empty library.")
  except json.JSONDecodeError:
    print("Error decoding JSON from library file. Starting with an empty library.")
  



def main(): 
  importLibrary()
  printDict()
  addSong("Have a good day based freestyle", "my names brandon thats my real name")
  addSong("Sooo Based Freestyle", "wanna hundred thousand")
  addSong("Sooo Based Freestyle", "I aint even stutter")
  addSong("Sooo Based Freestyle", "aint nun better")
  printDict()
  exportLibrary()


if __name__ == "__main__":
  main()