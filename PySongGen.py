#! /usr/bin/env python3
# Name: PySongGen
#
# Version: 0.0.1
#
# Author: Sinuhe Jaime Valencia
#
# Author_email: sierisimo@gmail.com
#
# Description:
#     Main code for running instances of pysonggen


from pysonggen import grammar
from pysonggen.songgen import SongG

gram = grammar.Grammar('./examples/example.mgram')

notes = None
audio = None
run = True

def get_phrase():
  global notes
  global audio
  notes = gram.expand(input("""Give a sentence for making a song.
It's very IMPORTANT that use spaces between every letter
Example: A A A B
  ->"""))
  audio = SongG(notes)
  print("Your song is now ready, it has: " + str(len(notes)) +" notes.")
  print("\n The length of the final song will be the same size, because we're using just one second per note")

def change_name():
  global audio

  print("Actual name is: "+audio.name+".ogg")
  print("Ok. Let's give the song an awesome Name:")
  name=input("New name: ")
  audio.name = name

def save_song():
  global audio
  if audio != None:
    audio.save_song()
  else:
    print("You have to make a song first...")


def print_notes():
  global audio
  if audio != None:
    print("There you are, this are your notes:")
    for i in audio.notes:
      print(i,end="  ")
  else:
    print("You haven't make a song first...")
  print("\n")


def exit_without_save():
  print("See you later aligator")

while run:
  options = {"s":save_song,
               "c":change_name,
               "n":get_phrase,
               "w":print_notes,
               "e":""
               }

  if audio == None:
    decision = input("""
    What do you want to do now?

n    Make a new song
e    Exit

Your choice: """)
  else:
    decision = input("""What do you want to do now?
s    Store Song (With default name: Song.ogg)
c    Change name of the song (The extension cannot be changed)
n    Make a new song
w    See the notes
e    Exit

Your choice: """)

  if len(decision) != 1 or not decision in list(options.keys()):
    print("Invalid Option. Please choose a valid one")
    continue
  elif decision == "e":
    exit_without_save()
    break

  options[decision]()
