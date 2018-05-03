from foo import Foo
from quit import Quit

if __name__ == '__main__':
    while True:
        text_input = raw_input('>')
        argv = [x for x in text_input.split(' ') if x]

        try:
            a = eval('%s()' % (argv[0][0].capitalize() + argv[0][1:]))
            a.execute(*argv[1:])
        except (NameError, SyntaxError):
            print argv
            print 'Undefined Command'