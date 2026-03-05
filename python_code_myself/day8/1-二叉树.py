class Node:
    def __init__(self, elem, lchild = None, rchild = None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

class BinaryTree:
    def __init__(self):
        self.root = None
        self.help_queue = []

    def level_build_tree(self,node:Node):
        if self.root is None:  # 树根为空
            self.root = node
            self.help_queue.append(node)
        else:
            self.help_queue.append(node)
            if self.help_queue[0].lchild is None:
                self.help_queue[0].lchild = node
            else:
                self.help_queue[0].rchild = node
                del self.help_queue[0]  # 出队

    def pre_order(self,current:Node):
        if current is None: return
        print(current.elem,end=' ')
        self.pre_order(current.lchild)
        self.pre_order(current.rchild)

    def mid_order(self,current:Node):
        if current is None: return
        self.mid_order(current.lchild)
        print(current.elem,end=' ')
        self.mid_order(current.rchild)

    def last_order(self, current_node: Node):
        if current_node:
            self.last_order(current_node.lchild)
            self.last_order(current_node.rchild)
            print(current_node.elem, end=' ')

    def level_order(self):
        help = []
        help.append(self.root)
        while help:
            out_node:Node = help.pop(0)
            print(out_node.elem,end=' ')
            if out_node.lchild:
                help.append(out_node.lchild)
            if out_node.rchild:
                help.append(out_node.rchild)



if __name__ == '__main__':
    tree = BinaryTree()
    for i in range(1,11):
        new_node = Node(i)
        tree.level_build_tree(new_node)  # 把节点放入tree中
    tree.pre_order(tree.root)
    print()
    tree.mid_order(tree.root)
    print()
    tree.last_order(tree.root)
    print()
    tree.level_order()