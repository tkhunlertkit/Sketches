from lib.utils import Utils

class Tree(object):

    def __init__(self, data=None, sub_trees=None):
        self._data = data
        self._id = None
        self._sub_trees = sub_trees if sub_trees else []

    @property
    def id(self):
        return self._id

    def set_node_id(self, curr_id):
        if not self._id:
            self._id = curr_id
            curr_id += 1
        return curr_id

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
        self._sub_trees.append(tree)

    def __str__(self):
        return str(self._data)

    def __iter__(self):
        if not self.data:
            return
        pos_child = [self]
        while pos_child:
            node = pos_child.pop()
            pos_child.extend(node.sub_trees)
            yield node

    def search_key(self, key):
        if len(self.sub_trees) == 1:
            return self.sub_trees[0]
        for sub_tree in self.sub_trees:
            if sub_tree.data == key:
                return sub_tree
        return self

    def is_leaf_node(self):
        return not self.sub_trees

    def visualize(self, output_filename, file_format_list):
        pos_child = [self]
        p2c_lut = {}
        node_id = 0
        used_id = set()
        dot_filename = output_filename + '.dot'
        with open(output_filename + '.dot', 'w') as f:
            f.write('digraph Tree {\n')
            f.write('\tremincross=true;\n')
            f.write('\toverlap=scalexy;\n')
            f.write('\tsplines=true;\n')
            f.write('\tnode [height=0.55];\n')
            while pos_child:
                node = pos_child.pop()
                node_id = node.set_node_id(node_id)
                pos_child.extend(node.sub_trees)
                p2c_lut[node.id] = node.data
                for child in node.sub_trees:
                    node_id = child.set_node_id(node_id)
                    f.write('\t%3s -> %3s;\n' % (node.id, child.id))
                    used_id.add(node.id)

            for i, j in sorted(p2c_lut.items()):
                node_desc = ['label="%s"' % j]
                if i not in used_id:
                    node_desc.append('peripheries=2,style=filled,color=green')
                if i == 0:
                    node_desc.append('style=filled,color=red')
                f.write('\t%3s [%s];\n' % (i, ','.join(node_desc)))
            f.write('}')

        Utils.execute_dot_file(dot_filename, file_format_list)

    def example(self):
        tree = Tree('start')
        t1 = Tree('t1')
        t1.add_sub_tree(Tree(3))
        t1.add_sub_tree(Tree(4))
        tree.add_sub_tree(t1)
        tree.visualize('test',['png'])