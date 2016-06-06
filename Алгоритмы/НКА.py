__author__ = 'Bogdan'
# encoding=utf-8

word = u''
transitions = {(0, u'a'): [1, 3], (0, u'b'): 2,
               (1, u'a'): 2, (1, u'b'): [0, 3],
               (2, u'a'): 2, (2, u'b'): 2,
               (3, u'a'): 1, (3, u'b'): 2}
final_states = [3, 2]


def fsm(word, transitions, final_states):
    value = 0
    i = 0
    while i < len(word):
        key = (value, word[i])
        value = transitions[key]
        i += 1
    if value in final_states:
        return True
    else:
        return False




def nsm(word, transitions, final_states):
    value = 0
    i = 0
    while i < len(word):
        key = (value, word[i])
        #print key
        values = transitions[key]
        i += 1
        if i == len(word):
            if isinstance(values, list):
                for v in values:
                    if v in final_states:
                        return True
                    else:
                        if v == final_states[-1]:
                            return False
            else:
                if values in final_states:
                    return True
                else:
                    return False
        try:
            for v in values:
                k = (v, word[i])
                for transition in transitions[k]:
                    if transition in final_states:
                        return True
                else:
                    return False
        except:
            k = (values, word[i])
            if transitions[k] in final_states:
                return True
            else:
                return False