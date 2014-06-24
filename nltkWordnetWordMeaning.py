# Load the wordnet corpus
from nltk.corpus import wordnet
 
# Get a collection of synsets (synonym sets) for a word
# Print the information
count = 0
for line in open("jun24.txt"):
  print "-" * 80
  count+=1
  synsets = wordnet.synsets(line.strip())
  print "%d) %s" %(count, line.strip())
  for synset in synsets:
    print "-" * 10
    print "%s(%s)" %(synset.name.split('.')[0],  synset.lexname.split('.')[0]) 
    print "Definition:", synset.definition
    for example in synset.examples:
      print "Example:", example
