from node import Node
from rb_tree import RBTree

if __name__=='__main__':
    n0 = Node(7)
    n1 = Node(3)
    n2 = Node(18)
    n3 = Node(10)
    n4 = Node(22)
    n5 = Node(8)
    n6 = Node(11)
    n7 = Node(26)
    n8 = Node(2)
    n9 = Node(6)
    n10 = Node(13)
    rb_tree = RBTree()
    rb_tree.insert(n0)
    rb_tree.insert(n1)
    rb_tree.insert(n2)
    rb_tree.insert(n3)
    rb_tree.insert(n4)
    rb_tree.insert(n5)
    rb_tree.insert(n6)
    rb_tree.insert(n7)
    rb_tree.out_graph()
    input()
    rb_tree.insert(n8)
    rb_tree.insert(n9)
    rb_tree.insert(n10)

    rb_tree.out_graph()
