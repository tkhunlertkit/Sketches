import config
from node import Node
from subprocess import call

class RBTree(object):

    def __init__(self):
        self.root = None

    def insert(self, node):
        node.set_color(config.RED)
        node.l_child = Node(None)
        node.r_child = Node(None)
        print('adding', node)
        if not self.root:
            self.root = node
        else:
            curr_node = self.root
            while curr_node:
                if node <= curr_node:
                    if curr_node.l_child.is_nil():
                        node.parent = curr_node
                        curr_node.l_child = node
                        break
                    curr_node = curr_node.l_child
                else:
                    if curr_node.r_child.is_nil():
                        node.parent = curr_node
                        curr_node.r_child = node
                        break
                    curr_node = curr_node.r_child
        self.resturcture(node)

    def resturcture(self, node):
        if node == self.root:
            print('root to black')
            node.set_color(config.BLACK)
        if node.parent and node.parent.color == config.RED:
            if node.uncle:
                if node.uncle.color == config.RED:
                    print('Recoloring')
                    node.parent.set_color(config.BLACK)
                    node.uncle.set_color(config.BLACK)
                    node.grandparent.set_color(config.RED)
                    self.resturcture(node.grandparent)
                elif node.uncle.color == config.BLACK:
                    # should be 4 resturcturing
                    if node.parent == node.grandparent.l_child:
                        if node == node.parent.l_child:
                            # left left case
                            print('left left case')
                            g = node.grandparent
                            p = node.parent
                            self.right_rotate(g)
                            g.switch_color()
                            p.switch_color()
                        else:
                            # Left Right case
                            print('left right case')
                            g = node.grandparent
                            self.left_rotate(node.parent)
                            self.right_rotate(g)
                            g.switch_color()
                            node.switch_color()
                    else:
                        if node == node.parent.r_child:
                            # Right Right case
                            print('right right case')
                            g = node.grandparent
                            p = node.parent
                            self.left_rotate(g)
                            g.switch_color()
                            p.switch_color()
                        else:
                            # Right Left Case
                            print('right left case')
                            g = node.grandparent
                            self.right_rotate(node.parent)
                            self.left_rotate(g)
                            g.switch_color()
                            node.switch_color()
                            pass
                new_root = self.root
                while new_root:
                    if not new_root.parent:
                        self.root = new_root
                    new_root = new_root.parent

    def right_rotate(self, node):
        g = node
        p = node.l_child

        if g.parent:
            if g.parent.l_child == g:
                g.parent.l_child = p
            else:
                g.parent.r_child = p
        p.parent = g.parent
        g.parent = p
        g.l_child = p.r_child
        p.r_child = g
        print(g)
        print(p)

    def left_rotate(self, node):
        g = node
        p = node.r_child

        if g.parent:
            if g.parent.l_child == g:
                g.parent.l_child = p
            else:
                g.parent.r_child = p
        p.parent = g.parent
        g.parent = p
        g.r_child = p.l_child
        p.l_child = g

    def inorder_traverse(self, node=None):
        # print(node)
        if not node:
            return
        if node.l_child:
            yield from self.inorder_traverse(node.l_child)
        yield node
        if node.r_child:
            yield from self.inorder_traverse(node.r_child)

    def out_graph(self):
        # self.inorder_traverse(self.root)
        with open('graph.dot', 'w') as f:
            f.write('digraph {\n')
            f.write('\tnode[shape=Mrecord]\n')
            for i in self.inorder_traverse(self.root):
                l_print = ''
                r_print = ''
                if not i.is_nil():
                    if not i.l_child.is_nil():
                        l_print = '\t' + str(i.value) + ':f0 -> ' + str(i.l_child.value) + ':f1\n'
                    if not i.r_child.is_nil():
                        r_print = '\t' + str(i.value) + ':f2 -> ' + str(i.r_child.value) + ':f1\n'
                    f.write(l_print)
                    f.write(r_print)
                    f.write('\t' + str(i.value) + ' [label="<f0>|<f1>' + str(i.value) + '|<f2>", style=filled, fillcolor=' + i.color + '];\n')
            f.write('}\n')
        call('dot graph.dot -Tsvg > graph.svg', shell=True)
        # for i in self.inorder_traverse(self.root):
        #     print(i)
