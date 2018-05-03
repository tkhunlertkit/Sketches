import itertools
from config import BOS, EOS, REGULAR, ADD_SMOOTH, SMOOTH
from text_handlers import get_sentence_from_file, subseq_word

list_of_options = [REGULAR, SMOOTH, ADD_SMOOTH]

class DictionaryModel(object):

    def __init__(self, delta):
        if delta > 1 or delta < 0:
            print 'USAGE: 0 <= delta <= 1'
            exit()

        self.delta = delta
        self.tally_version = 0
        self.prob_version = 0
        self.word_collection = set()
        self.number_of_occurrences = {}
        self.word_link = {}
        self.prob_link = {}
        self.top = dict({
            REGULAR: 0.0,
            SMOOTH: 1.0,
            ADD_SMOOTH: delta
        })
        self.bottom = dict({
            REGULAR: 0.0
        })

    def get_num_word(self):
        return len(self.word_collection)

    def get_word_list(self):
        return self.word_collection.copy()

    def tally(self, file_name):
        self.tally_version += 1
        for line in get_sentence_from_file(file_name):
            for (i, j) in subseq_word(line):
                self.inc_tally(i, j)
                self.record(i)
            self.record(j)

    def inc_tally(self, f, to):
        if f not in [BOS, EOS]:
            self.word_collection.add(f)
        if to not in [BOS, EOS]:
            self.word_collection.add(to)
        if f not in self.word_link:
            self.word_link[f] = {}
        if to not in self.word_link[f]:
            self.word_link[f][to] = 1
        else:
            self.word_link[f][to] += 1

    def record(self, word):
        if word not in self.number_of_occurrences:
            self.number_of_occurrences[word] = 1
        else:
            self.number_of_occurrences[word] += 1

    def calc_prob(self):
        self.prob_version += 1

        self.bottom[SMOOTH] = self.get_num_word()
        self.bottom[ADD_SMOOTH] = self.bottom[SMOOTH] * self.delta
        print self.top[ADD_SMOOTH], self.bottom[ADD_SMOOTH]

        for option in list_of_options:
            self.calc_prob_with_option(option=option)

        # print '%10s  %12s  %12s  %15s  %10s  %10s  %10s  %10s' % ('option', 'from', 'to', 'prob[from][to]', 'num[from][to]', 'num[from]', 'top[option]', 'bottom[option]')
        # print '%10s  %12s  %12s  %15.6f  %10s  %10s  %10s  %10s' % (option, f, to, self.prob_link[option][f][to], self.word_link[f][to], self.number_of_occurrences[f], self.top[option], self.bottom[option])

    def calc_prob_with_option(self, option):
        if option not in self.prob_link:
            self.prob_link[option] = {}

        for f in self.word_link:
            if f != BOS and f != EOS:
                self.word_collection.add(f)

            if f not in self.prob_link[option]:
                self.prob_link[option][f] = {}
            for to in self.word_link[f]:
                numer = self.top[option] + self.word_link[f][to]
                denom = self.number_of_occurrences[f] + self.bottom[option]
                self.prob_link[option][f][to] = numer / denom
                # if f == BOS:
                #     print f, to, self.prob_link[option][f][to]



    def get_prob(self, fr, to, option=REGULAR):
        # print fr, to
        if fr in self.prob_link[option]:
            if to in self.prob_link[option][fr]:
                return self.prob_link[option][fr][to]


        # print fr, to
        if fr not in self.number_of_occurrences:
            return 0
        else:
            return self.top[option] / (self.number_of_occurrences[fr] + self.get_num_word())
        #
        # list_words.add(BOS)
        # list_words.add(EOS)
        # for (i, j) in itertools.permutations(list_words, 2):
        #     if i not in self.prob_link:
        #         self.prob_link[i] = {}
        #     if j not in self.prob_link[i]:
        #         if i not in number_of_occurrences:
        #             self.prob_link[i][j] = 0
        #         else:
        #             self.prob_link[i][j] = top / number_of_occurrences[i]

    def get_next_word(self, current_word, option=REGULAR):
        from config import PRECISION
        sum = 0
        for word in self.get_word_list():
            # if current_word != word:
            prob = self.get_prob(current_word, word, option=option)
            sum += prob
            print '%15s -> %15s: %.*f' % (current_word, word, PRECISION, prob)
        print sum
