from main import subseq_word

def get_sentence_from_file(file_name):
    with open(file_name) as f:
        # buff = ''
        # for line in f:
        #     if line != '\n':
        #         buff += line.strip('\n')
        #         # print '>>', buff
        #         while '.' in buff:
        #             i = buff.index('.')
        #             sent, buff = buff[:i], buff[i+1:]
        #
        #             yield sent.strip()
        # if buff:
        #     yield buff.strip()
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

if __name__ == '__main__':

    file_name = 'text.txt'
    for s in get_sentence_from_file(file_name):
        print s
        print
        for (i,j) in subseq_word(s):
            print i, j
