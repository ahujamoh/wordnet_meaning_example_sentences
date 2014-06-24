# Load the wordnet corpus
from nltk.corpus import wordnet
 
 
#file format should be "one word per line"
count = 0
for line in open("jun24.txt"):
  print "-" * 80
  count+=1
  # Get a collection of synsets for a word
  synsets = wordnet.synsets(line.strip())
  # Print the information
  print "%d) %s" %(count, line.strip())
  for synset in synsets:
    print "-" * 10
    print "%s(%s)" %(synset.name.split('.')[0],  synset.lexname.split('.')[0]) 
    print "Definition:", synset.definition
    for example in synset.examples:
      print "Example:", example
