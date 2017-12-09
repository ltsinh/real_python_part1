import random
 
nouns = ["dog", "cat", "horse", "chicken", "rooster", "sheep", "cow"]
verbs = ["kicks", "runs", "bounces", "slurps", "jumps", "sleeps", "rolls"]
adjectives = ["big", "small", "huge", "medium", "tall", "fat"]
adverbs = ["carefully", "quickly", "lazily", "effortlessly", "quietly"]
 
def make_poem():
  adj = random.choice(adjectives)
  noun = random.choice(nouns)
  verb = random.choice(verbs)
  adverb = random.choice(adverbs)
  
  sentence = " ".join([adj, noun, verb, adverb])
  sentence = "A " + sentence + ".\n"

  return sentence

def save_sentence(sentence, handle):
  if handle.closed: return;
  handle.write(sentence)
 
file = "poem.txt"
f = open(file, 'w')
for i in range(4):
  save_sentence(str(i) + " " + make_poem(), f)
f.close()
