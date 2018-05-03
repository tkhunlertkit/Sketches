import sys
from config import DEBUG, REGULAR, SMOOTH, ADD_SMOOTH, DELTA, BOS, EOS
from language_model.dictionary_model import DictionaryModel
from language_model.prediction_model import print_dict, print_all_prob_from_sentence

prob_no_smooth = {}
prob_smooth = {}
prob_add_smooth = {}

def make_dict(mode, suffix):
    return dict({
            'mode': mode,
            'suffix': suffix
        })

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'USAGE: python main.py <file_input>'
        exit()

    file_name = sys.argv[1]
    prob_model = DictionaryModel(DELTA)
    print 'reading the book...'
    prob_model.tally(file_name)
    prob_model.calc_prob()
    print 'Done reading book.'


    print 'Calculating Probabilities'
    list_of_prob = []

    print '    -Regular'
    list_of_prob.append(make_dict(REGULAR, 'Regular'))

    print '    -Smooth'
    list_of_prob.append(make_dict(SMOOTH, 'Smooth'))

    print '    -Additive Smoothing'
    list_of_prob.append(make_dict(ADD_SMOOTH, 'additive smooth with delta = %.1f' % DELTA))

    print 'Done calculating probabilities'

    if DEBUG:
        print
        print_dict(d, 'tally')
        print
        print_dict(prob_no_smooth, 'P')
        print get_num_word(prob_no_smooth)

    print '\n-------------------------------------------------------------'
    print '\nStats:'
    num_word = prob_model.get_num_word()
    print
    print 'total number of words:', num_word
    print_all_prob_from_sentence(prob_model, list_of_prob, 'John read a book')
    print_all_prob_from_sentence(prob_model, list_of_prob, 'Cher read a book')
    print_all_prob_from_sentence(prob_model, list_of_prob, 'test this')
    print_all_prob_from_sentence(prob_model, list_of_prob, 'call me ishmael')
    print_all_prob_from_sentence(prob_model, list_of_prob, 'we desire increase')

    current_word = 'has'
    print prob_model.get_next_word(current_word, option=SMOOTH)
