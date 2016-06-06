#>12 words
import random

def noun():
    nouns = [u'pollution', u'Pierre de Coubertin', u'Chomsky', u'hound', u'octopus', u'evolution', u'bear', u'mafia', u'pancake', u'pand']
    return random.choice(nouns)

def adverb():
    nouns = [u'loudly', u'calmly', u'passionately', u'playfully', u'unhappily', 'ironically', u'intentionally', u'madly', u'furiously',
             u'openly', u'agressively', u'merrily', u'dangerously', u'lazily', u'attentively']
    return random.choice(nouns)


def adjective(word):
    adjectives = [u'awesome', u'courageous', u'ancient', u'excited', u'green', u'invisible', u'invincible', u'lazy', u'amazed']
    return random.choice(adjectives) + u' ' + word

def intensifier(adj):
    intensifiers = [u'very', u'partly', u'super', u'abnormally', u'obviously']
    random_intensifier = random.choice(intensifiers)
    result = random_intensifier + u' ' + adj
    return result

def verb_of_thought(subj):
    verbs = [u'thinks', u'knows', u'supposes', u'is convinced', u'believes', u'suggests', u'hopes', u'understands']
    return subj + u' ' + random.choice(verbs)

def verbs(subj, obj):
    verbs = [u'hug', u'kill', u'look after', u'punch', u'feed', u'greet', u'adore', u'generate', u'catch', u'torture']
    return subj + u' ' + random.choice(verbs) + u' ' + obj

def sentence_part():
    x = adjective(noun()) + u's'
    y = u'not ' + adjective(noun()) + u's' + ', but ' + adjective(noun()) + u's'
    z = u'not only '+ adjective(noun()) + u's' + ', but also ' + adjective(noun()) + u's'
    b = random.choice([x, y, z])
    return b

def another_part():
    x = verbs(noun() +'s', noun()) + '.'
    f = adverb() + u' ' + verbs(noun() +'s', noun()) + '.'
    z = verbs(noun() + u's', noun()) + ' and say: \"' + noun() + ' is ' + adjective(noun()) + '!' + '\"'
    b = random.choice([x, z])
    return b

def part():
    z = adjective(noun())
    y = intensifier(adjective(noun()))
        
    b = random.choice([y, z])
    return b


def random_sentence():
    sentence = verb_of_thought(part()) + u' that ' + verbs(sentence_part(), noun()) + u', ' + u'because ' + another_part()
    
    return sentence


print random_sentence()
