import os

def copy(text):
    os.system("echo '%s' | pbcopy" % text)

def paste():
    os.system("pbpaste")

def line_generator(filename):
    whole_text = ""
    with open(filename, 'r') as f:
        for line in f:
            whole_text += line
    list_of_text = whole_text.split("//")
    for text in list_of_text:
        yield text.strip()


if __name__ == '__main__':
    filename = 'copy_text.txt'
    read_file = line_generator(filename)
    # for line in read_file:
    #     print line.strip()
    try:
        while True:
            raw_input('press enter')
            copy(next(read_file))
            paste()
    except:
        print "all text copied and paste."
    # for i in range(10):
    #     try:
    #         text = next(read_file)
    #         print text
    #     except:
    #         pass
