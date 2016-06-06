#прога генерирует странные предложения.
import random

def noun():
    nouns = [u'keyboeard', u'master of mic', u'cow', u'le parkour', u'Jack Sparrow', u'Nissan',
             u'beats by dr.Dre', u'Eminem', u'Dublin', u'CPU']
    return random.choice(nouns)

def adverb():
    nouns = [u'quickly', u'undoubtebly', u'slowly', u'deeply', u'badly', 'early', u'seriously', u'nearly',
             u'fully', u'exactly', u'fast', u'certainly', u'dangerously', u'loudly', u'carefully']
    return random.choice(nouns)


def adjective(word):
    adjectives = [u'awesome', u'fast', u'bad', u'wide', u'left', u'old', u'far', u'able', u'single']
    return random.choice(adjectives) + u' ' + word

def intensifier(adj):
    intensifiers = [u'quite', u'rather', u'very']
    random_intensifier = random.choice(intensifiers)
    result = random_intensifier + u' ' + adj
    return result

def verb_of_thought(subj):
    verbs = [u'thinks', u'knows', u'supposes', u'is convinced', u'believes', u'suggests', u'hopes',
             u'understands']
    return subj + u' ' + random.choice(verbs)

def verbs(subj, obj):
    verbs = [u'kill', u'ill', u'use', u'make', u'eat', u'meet', u'love', u'CODE', u'climb', u'run']
    return subj + u' ' + random.choice(verbs) + u' ' + obj

def sentence_part():
    a = adjective(noun()) + u's'
    b = u'not only' + adjective(noun()) + u's' + ', but ' + adjective(noun()) + u's'
    c = u'if not '+ adjective(noun()) + u's' + ', then ' + adjective(noun()) + u's'
    e = random.choice([a, b, c])
    return e

def second_part():
    x = verbs(noun() +'s', noun()) + '.'
    f = adverb() + u' ' + verbs(noun() +'s', noun()) + '.'
    b = random.choice([x, f])
    return b

def part():
    a = adjective(noun())
    b = intensifier(adjective(noun()))
        
    c = random.choice([a, b])
    return c

def conjunctions():
    a = u'that'
    b = u'because'
    c = u''
    e = random.choice([a, b, c])
    return e

def random_sentence():
    sentence = verb_of_thought(part()) + u' ' + conjunctions()+ u' ' + verbs(sentence_part(), noun()) + u', ' +\
               conjunctions() + u' ' + second_part()
    
    return sentence


print random_sentence()
