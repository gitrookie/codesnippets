class Tree:
    class Node:
        def __init__(self, x=None):
            self.x = x
            self.ltchild = None
            self.rtchild = None

    def __init__(self, *args):
        if not args:
            self.root = Tree.Node()
        else:
            self.root = Tree.Node(args[0])
        for ob in args[1:]:
            node = Tree.Node()
            self.add_node(ob, node)

    def add_node(self, val):
        if self.root.x is None:
            self.root.x = val
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if node.x is not None:
            if node.x > val:
                node = node.ltchild
                self._add(val, node)
            elif node.x < val:
                node = node.rtchild
                self._add(val, node)
        else:
            node = Tree.Node(val)

    def traverse(self):

t = Tree()
