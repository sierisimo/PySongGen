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

while True:
#  print(gram)
  notes = gram.expand(input("""Give a sentence for making a song.
It's very IMPORTANT that use spaces between every letter
Example: A A A B
  ->"""))
  audio = SongG(notes)
