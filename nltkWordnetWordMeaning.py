import sys
# Load the wordnet corpus
from nltk.corpus import wordnet
 
 
#file format should be "one word per line"
file_list = []
for x in sys.argv[1:]:
  file_list.append(x)
count = 0
for filename in file_list:
  for line in open(filename):
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
