# Name: Grammar
#
# Version: 0.1.0
#
# Author: Sinuhe Valencia
#
# Author_email: sierisimo@gmail.com
#
# Description:
#   Group of classes and functions that helps to make the parsing of grammar files easy.

class ParseGrammar():
  """A function for parsing grammar files."""
  def __init__(self,src):
    extension = src.split('.')[-1]
    if extension != 'mgram':
      raise ParsingExceptionError("Extension for simple grammar is 'mgram',founded was: "+extension)
    self.src = src
  def parse_rules(self):
    rules = {}

    with open(self.src,"rt") as grammar_file:
      line_number = 0
      while True:
          in_line = grammar_file.readline()
          if not in_line:
              break
          in_line = in_line[:-1]
          line_number = line_number + 1
          statement = in_line.split('::')

          #This are the syntax checks
          first_c = "<" in statement[0]
          second_c = ">" in statement[0]
          third_c = "::" in in_line
          fourth_c = "=" in statement[1]

          if not first_c:
            raise ParsingExceptionError("Missing '<' at line: "+str(line_number)+"  in statement: "+in_line)
          if not second_c:
            raise ParsingExceptionError("Missing '>' at line: "+str(line_number)+"  in statement: "+in_line)
          if not third_c:
            raise ParsingExceptionError("Missing '::' at line: "+str(line_number)+"  in statement: "+in_line)
          if not fourth_c:
            raise ParsingExceptionError("Missing '=' at line: "+str(line_number)+"  in statement: "+in_line)

          rule = statement[0]
          cons = statement[1].split('=')[-1]

          rule = rule.split('<')[-1].split('>')[0]

          if "'" not in cons:
            tmp_list = cons.split("<")[1:]
            cons_list = []
            for i in tmp_list:
              i = i.split(">")[0]
              cons_list.append(i)
            else:
              cons = cons_list

          if rule in rules:
            rules[rule].append(cons)
          else:
            rules[rule] = [cons]

    grammar_file.close()

    return rules


class Grammar():
  """Just a simple class that holds the information of the parsing """
  def __init__(self,file_name):
    parser = ParseGrammar(file_name)
    self.rules = parser.parse_rules()

  def get_a_tree(self,deep=3):


  def __str__(self):
    return "Grammar: \n"+str(self.rules)


class ProbabilisticGrammar():
  """A class that holds the information of parsing a probabilistic grammar file"""
  def __init__(self):
    pass


class ParsingExceptionError(Exception):
  """Class for letting the user know that his file name is wrong"""
  def __init__(self,value):
    self.value = value
  def __str__(self):
    return repr(self.value)
