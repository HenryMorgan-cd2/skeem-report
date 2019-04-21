#!/usr/bin/env python

"""
Pandoc filter to convert all level 2+ headers to paragraphs with
emphasized text.
"""

from pandocfilters import toJSONFilter, Strong, Para, stringify, RawInline, BlockQuote, RawBlock, Str
import json


filename = "./bin/debuglog.log" 
debugFile = open(filename, 'w')

def p(thing):
  debugFile.write(thing.encode('utf8'))
  debugFile.write("\n")

def latex(s):
    return RawBlock('latex', s)

def notequote(key, value, format, meta):
  if key == 'BlockQuote' and format == 'latex':
    if stringify(value).startswith(":note"):
      p(json.dumps(value[0]['c'][0]))
      value[0]['c'][0] = Strong([Str("Note:")]) # remove the ":note" prefix
      p(json.dumps(value))
      return [latex("\\begin{noteQuote}")] + value + [latex("\\end{noteQuote}")]


if __name__ == "__main__":
  toJSONFilter(notequote)
  debugFile.close()
