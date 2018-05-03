from tree import Tree

class TreeNode(object):
    def __init__(self, data=None, sub_trees=[]):
        self._data = data
        self._sub_trees = sub_trees

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def sub_trees(self):
        return self._sub_trees

    def add_sub_tree(self, tree):
        if not isinstance(tree, Tree):
            return
        for t in tree:
            print (t)
        self._sub_trees.append(tree)

    def __str__(self):
        return str(self._data)

