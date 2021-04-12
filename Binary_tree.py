class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BinaryTree:
    def __init__(self,root):
        self.root=TreeNode(root)
    def print_tree(self,traversal_type):
        if(traversal_type=='preorder'):
            print(self.preorder(self.root,'')[:-1])
        elif(traversal_type=='inorder'):
            print(self.inorder(self.root,'')[:-1])
        elif(traversal_type=='postorder'):
            print(self.postorder(self.root,'')[:-1])
        else:
            print('Invalid traversal type!')
    def preorder(self,start,traversal):
        if(start):
            traversal=traversal+str(start.data)+'-'
            traversal=self.preorder(start.left,traversal)
            traversal=self.preorder(start.right,traversal)
        return(traversal)
    def inorder(self,start,traversal):
        if(start):
            traversal=self.inorder(start.left,traversal)
            traversal=traversal+str(start.data)+'-'
            traversal=self.inorder(start.right,traversal)
        return(traversal)
    def postorder(self,start,traversal):
        if(start):
            traversal=self.postorder(start.left,traversal)
            traversal=self.postorder(start.right,traversal)
            traversal=traversal+str(start.data)+'-'
        return(traversal)

        #         1
        #       /   \
        #     2       3
        #   /  \     /  \
        #  4    5    6   7
def preorder(node):
    stack=list()
    while(True):
        if(node):
            stack.append(node)
            print(node.data)
            node=node.left
        elif(stack):
            node=stack.pop()
            node=node.right
        else:
            break
def inorder(node):
    stack=list()
    while(True):
        if(node):
            stack.append(node)
            node=node.left
        elif(stack):
            node=stack.pop()
            print(node.data)
            node=node.right
        else:
            break
tree = BinaryTree(1)
tree.root.left=TreeNode(2)
tree.root.right=TreeNode(3)
tree.root.left.left=TreeNode(4)
tree.root.left.right=TreeNode(5)
tree.root.right.left=TreeNode(6)
tree.root.right.right=TreeNode(7)
tree.print_tree('preorder')
tree.print_tree('inorder')
tree.print_tree('postorder')
preorder(tree.root)
