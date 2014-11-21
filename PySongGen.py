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

gram = grammar.Grammar('./examples/example.mgram')

print(gram)