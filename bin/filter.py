#!/usr/bin/env python

"""
Pandoc filter to convert all level 2+ headers to paragraphs with
emphasized text.
"""

from pandocfilters import toJSONFilter, toJSONFilters, Strong, Para, Header, stringify, RawInline, BlockQuote, RawBlock, Str
import json
import re


filename = "./bin/debuglog.log" 
debugFile = open(filename, 'w')

def p(thing):
  debugFile.write(thing.encode('utf8'))
  debugFile.write("\n")

def latex(s):
    return RawBlock('latex', s)

def titleize(text):
  def isException(word):
    # is word in exception list or is it all caps with an optional "s" e.g DVI or VGAs
    exceptions = ['the', 'a', 'and', 'vs']
    return (word in exceptions ) or re.match("^[A-Z]+s?$", word)

  return ' '.join([word if isException(word) else word.title() for word in text.split()])

################ FILTERS
################ FILTERS
################ FILTERS
################ FILTERS

def customQuote(tag, prefix, blockName):
  def replaceQuote(key, value, format, meta):
    if key == 'BlockQuote' and format == 'latex':
      if stringify(value).startswith(":" + tag):
        value[0]['c'][0] = Strong([Str(prefix)]) # remove the ":note" prefix
        return [latex("\\begin{"+ blockName +"}")] + value + [latex("\\end{"+ blockName +"}")]
  return replaceQuote

noteQuote = customQuote("note", "Note:", "noteQuote")
commentQuote = customQuote("comment", "Comment:", "commentQuote")


def titlizeHeadings(key, value, format, meta):
  if (key == 'Header'):
    size, meta, text = value
    titled = titleize(stringify(text))
    return Header(size, meta, [Str(titled)])

filters = [
  titlizeHeadings,
  noteQuote,
  commentQuote,
]


if __name__ == "__main__":
  toJSONFilters(filters)
  debugFile.close()
