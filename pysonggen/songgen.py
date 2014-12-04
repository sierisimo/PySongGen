# Name: pysonggen
#
# Version: 0.0.1
#
# Author: Sinuhe Jaime Valencia
#
# Author_email: sierisimo@gmail.com
#
# Description:
#      Main file for the project PySongGen

from pydub import AudioSegment

import os
#import sys for using: sys.path[0]

EXTENSION = "ogg"
PREFIX = "mnotes"
NOSOUND = "muted"

class SongG():
  """Class for Generate songs"""
  def __init__(self,notes):
    """Constructor of class"""
    if type(notes) != list:
      raise TypeError("Expected a list, arguments is: " + str(type(notes)))

    self.notes = notes
    self.name = "PySong"

    files = {}
    song = None

    t_files_l = []
    for n in notes:
      file_name = n.split("'")[1]

      if file_name != "-":
        file_name = file_name + "." + EXTENSION

      else:
        file_name = NOSOUND + "." + EXTENSION

      if not file_name in t_files_l:
        files[n] = AudioSegment.from_ogg(os.getcwd()+"/"+PREFIX+"/"+file_name)
        t_files_l.append(file_name)

      if song == None:
        song = files[n][:1000]
      else:
        song = song[:] + files[n][:1000]

    self.files = files
    self.song = song

  def save_song(self):
    self.song.export(self.name+"."+EXTENSION,format="ogg")
    print("Song saved in:"+str(os.getcwd())+"/"+self.name+"."+EXTENSION)
