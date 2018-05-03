class Foo(object):

    def execute(self, *wargs):
        print 'in foo'
        for arg in wargs:
            print arg