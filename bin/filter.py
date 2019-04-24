#!/usr/bin/env python

"""
Pandoc filter to convert all level 2+ headers to paragraphs with
emphasized text.
"""

from pandocfilters import toJSONFilter, toJSONFilters, Strong, Para, Header, stringify, RawInline, BlockQuote, RawBlock, Str
import json


filename = "./bin/debuglog.log" 
debugFile = open(filename, 'w')

def p(thing):
  debugFile.write(thing.encode('utf8'))
  debugFile.write("\n")

def latex(s):
    return RawBlock('latex', s)

def titleize(text):
  exceptions = ['the', 'a', 'and', 'vs']
  return ' '.join([word if word in exceptions else word.title() for word in text.split()])

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
