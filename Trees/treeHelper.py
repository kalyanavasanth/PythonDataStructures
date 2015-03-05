#!usr/bin/python3
'''
Created on 05-Mar-2015

@author: SESA366034
'''
class Tree():
    class Node():
        def __init__(self):
            self.data=None
            self.left=None
            self.right=None
            
    def __init__(self):
        self.root=None
        
    def setRoot(self,data):
        self.root=data
        
    def createNode(self,data):
        self.node,self.node.data=Tree().Node(), data
        return self.node
    
    def inOrder(self, node):
        if node==None:
            return
        self.inOrder(node.left)
        print(node.data)
        self.inOrder(node.right)

    def preOrder(self, node):
        if node==None:
            return
        print(node.data)
        self.preOrder(node.left)
        self.preOrder(node.right)
        
    def postOrder(self, node):
        if node==None:
            return
        self.postOrder(node.left)
        self.postOrder(node.right)
        print(node.data)
                
def main():
    tree=Tree()
    tree.setRoot(tree.createNode(1))
    tree.root.left=tree.createNode(2)
    tree.root.right=tree.createNode(3)
    tree.inOrder(tree.root)
    tree.preOrder(tree.root)
    tree.postOrder(tree.root)
    
if __name__=="__main__": main()