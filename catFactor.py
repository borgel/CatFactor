#!/usr/bin/env python

'''
http://en.wikipedia.org/wiki/Cat
The library:
https://wikipedia.readthedocs.org/en/latest/quickstart.html#quickstart
'''

from wikipedia import wikipedia
from random import choice
import nltk.data
import argparse

SOURCE_PAGE_NAMES = [
      'Cat'
      ]



def traverseDepth(page, depth):
   '''
   Traverse 'depth' links down, starting at 'page'. Returns another wikipedia.page
   '''
   print 'going to depth ' + str(depth)

   #TODO make this work

   return page

def selectSentences(section, sentences):
   '''
   Select a random sentence, then grab that one and 'sentences' more after it
   '''
   print 'selecting ' + str(sentences) + ' sentences'

   # TODO make this work

   #get number of sentences - # to pull
   tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
   sens = tokenizer.tokenize(section)

   #slice off the last # elements of the list
   sensLimited = sens[:-sentences]
   totalSens = len(sensLimited)

   #print sens
   #print sensLimited

   # go a random sentence
   sen = choice(sensLimited)

   # pull it
   # FIXME pull following

   return sen



print 'Cat Factor Starting'

# gotta set a ratelimit :(
wikipedia.set_rate_limiting(True)

# get passed options
parser = argparse.ArgumentParser()
parser.add_argument('-l', '--layers', dest='NumLayers', type=int, default=0, help='The number of layers down to traverse')

parser.add_argument('-s', '--sentences', dest='NumSentences', type=int, default=1, help='The number of contiguous sentences to pull')
args = parser.parse_args()

print 'layers down = ' + str(args.NumLayers)
print 'sentences in = ' + str(args.NumSentences)

if args.NumLayers < 0 or args.NumLayers > 10:
   print 'Too many or too few layers'
   exit()
if args.NumSentences < 1 or args.NumSentences > 10:
   print 'Too many or too few sentences'
   exit()

# randomly choose a page to start at from the list
pageName = choice(SOURCE_PAGE_NAMES)

# get the page
page = wikipedia.page(pageName)

# for each depth to traverse,
   # randomly choose a link to go down
page = traverseDepth(page, args.NumLayers)

# randomly choose a section. Keep trying until you find one that has content
# (they may be empty). Dont try toooo many times
sectionTitle = ''
section = ''
remaining = len(page.sections)
while remaining > 0:
   print '.'
   sectionTitle = choice(page.sections)
   section = page.section(sectionTitle)

   if len(section) > 0:
      break
   remaining -= 1
if remaining == 0:
   print 'Didnt find any not empty sections'
   exit()

print sectionTitle + ":"

# take the some sentences
words = selectSentences(section, args.NumSentences)

print 'Final words are...\n'
print words
