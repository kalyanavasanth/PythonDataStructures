from treeHelper import Tree

def main():
    tree=Tree()
    tree.setRoot(tree.createNode(1))
    tree.root.left=tree.createNode(2)
    tree.root.right=tree.createNode(3)
    tree.root.left.left=tree.createNode(4)
    tree.inOrder(tree.root)
    tree.preOrder(tree.root)
    tree.postOrder(tree.root)
    tree.rootToLeafPaths(tree.root)
    
if __name__=="__main__": main()