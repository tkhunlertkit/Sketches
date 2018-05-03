import tensorflow as tf
import urllib
import os
import zipfile
import collections
import numpy as np
import random

data_index = 0
# generate batch data
def generate_batch(data, batch_size, num_skips, skip_window):
    global data_index
    assert batch_size % num_skips == 0
    assert num_skips <= 2 * skip_window
    batch = np.ndarray(shape=(batch_size), dtype=np.int32)
    context = np.ndarray(shape=(batch_size, 1), dtype=np.int32)
    span = 2 * skip_window + 1  # [ skip_window input_word skip_window ]
    buffer = collections.deque(maxlen=span)
    print()
    for _ in range(span):
        print(data_index)
        print(buffer)
        buffer.append(data[data_index])
        data_index = (data_index + 1) % len(data)
    print()
    for i in range(batch_size // num_skips):
        print(i)
        target = skip_window  # input word at the center of the buffer
        targets_to_avoid = [skip_window]
        for j in range(num_skips):
            while target in targets_to_avoid:
                target = random.randint(0, span - 1)
            targets_to_avoid.append(target)
            batch[i * num_skips + j] = buffer[skip_window]  # this is the input word
            context[i * num_skips + j, 0] = buffer[target]  # these are the context words
        buffer.append(data[data_index])
        data_index = (data_index + 1) % len(data)
    # Backtrack a little bit to avoid skipping words in the end of a batch
    data_index = (data_index + len(data) - span) % len(data)
    return batch, context

def maybe_download(filename, url, expected_bytes):
    if not os.path.exists(filename):
        print('File not found. Prepare to download.')
        try:
            print('Downloading...')
            filename, _ = urllib.request.urlretrieve(url + filename, filename)
            print('Downloaded:', filename)
            return filename

        except urllib.error.HTTPError as error:
            print(error)

    else:
        return filename

def read_data(filename):
    with zipfile.ZipFile(filename) as f:
        data = tf.compat.as_str(f.read(f.namelist()[0])).split()

    return data

def build_dataset(words, n_words):
    count = [('UNK', -1)]
    count.extend(collections.Counter(words).most_common(n_words - 1))
    dictionary = dict()
    data = list()
    unk_count = 0

    for ((word, _), word_id) in zip(count, range(n_words)):
        dictionary[word] = word_id

    for word in words:
        index = 0
        if word in dictionary:
            index = dictionary[word]
        else:
            index = 0
            unk_count += 1
        data.append(index)

    count[0] = ('UNK', unk_count)
    reversed_dict = dict(zip(dictionary.values(), dictionary.keys()))

    return data, count, dictionary, reversed_dict

if __name__ == '__main__':
    url = 'http://mattmahoney.net/dc/'
    filename = 'text8.zip'
    num_words_in_dict = int(1e5)
    batch_size = 128
    embedding_size = 128  # Dimension of the embedding vector.
    skip_window = 1       # How many words to consider left and right.
    num_skips = 2

    num_steps = 100


    print('Obtaining File...')
    filename = maybe_download(filename, url, 31344016)

    print('Unpacking Data...')
    words = read_data(filename)

    print('Building Dataset...')
    data, count, dictionary, reversed_dict = build_dataset(words, num_words_in_dict)

    for word, word_id in zip(words[:20], data[:20]):
        print(word, word_id)

    for step in range(num_steps):
        batch_inputs, batch_context = generate_batch(data, batch_size, num_skips, skip_window)
        for word_ind in batch_inputs:
            print(word_ind, words[word_ind])
        print
        print()
        for word_ind in batch_context:
            print(word_ind, words[word_ind[0]])
        input('waiting...')
