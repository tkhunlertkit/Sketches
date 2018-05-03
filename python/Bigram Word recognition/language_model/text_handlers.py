import re
from config import BOS, EOS

def get_sentence_from_file(file_name):
    with open(file_name) as f:
        cumulative_line = ''
        for line in f:
            if line != '\n':
                cumulative_line += line.replace('\n', ' ')
                sentences = list(reversed(cumulative_line.split('.')))

                while len(sentences) > 1:
                    # found at least one sentences
                    yield(sentences.pop().strip())
                cumulative_line = sentences.pop()

    if cumulative_line.strip():
        yield(cumulative_line.strip(' .'))

def subseq_word(sentence):
    line = BOS + ' ' + sentence.rstrip('\.\n') + ' ' + EOS
    line = line.lower()
    # print line
    elems = re.split('\W+ ', line)
    # elems = line.split(' ')
    # print elems
    end = len(elems)
    for i,j in zip(elems[:end - 1], elems[1:end]):
        yield(i, j)
