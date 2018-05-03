import config

class Node(object):

    def __init__(self, value, color=config.BLACK, parent=None):
        self.value = value
        self.parent = parent
        self.l_child = None
        self.r_child = None
        self.color = color

    # def __eq__(self, other):
    #     print('comparing...eq', self.value, other.value)
    #     return False

    # def __lt__(self, other):
    #     print('comparing...lt', self.value, other.value)
    #     return False

    def __le__(self, other):
        return self.value <= other.value

    def __str__(self):
        return str(self.value) + ' :: ' + self.color + ' :: p:' + (str(self.parent.value) if self.parent else 'None')

    def set_color(self, color):
        self.color = color

    def switch_color(self):
        self.color = config.BLACK if self.color == config.RED else config.RED

    def is_nil(self):
        return not self.value

    @property
    def grandparent(self):
        return self.parent.parent if self.parent else None

    @property
    def uncle(self):
        if self.grandparent:
            if self.grandparent.l_child == self.parent:
                return self.grandparent.r_child
            else:
                return self.grandparent.l_child
        else:
            return None