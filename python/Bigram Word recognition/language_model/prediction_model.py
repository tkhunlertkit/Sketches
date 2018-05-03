from text_handlers import subseq_word
from config import PRECISION
from dictionary_model import DictionaryModel

def prob_given_sentence(prob_model, mode, sentence):
    p = 1
    for (i, j) in subseq_word(sentence):
        prob = prob_model.get_prob(i, j, mode)
        p = p * prob
    return p

def print_dict(d, prefix):
    for f in d:
        for to in d[f]:
            print '%s(%10s, %10s)\t= %.*f' % (prefix, f, to, PRECISION, d[f][to])

def print_sentence_with_prob(prob_model, mode, sentence, suffix='Regular'):
    p = prob_given_sentence(prob_model, mode, sentence)
    print 'P( %-20s ) = %16.*f  (%s)' % (sentence, PRECISION, p, suffix)
    return p

def print_all_prob_from_sentence(prob_model, list_of_prob, sentence):
    for prob in list_of_prob:
        print_sentence_with_prob(prob_model, prob['mode'], sentence, prob['suffix'])
    print
