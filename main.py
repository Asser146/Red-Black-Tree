from RB_Tree import Tree

tree=Tree()
for i in range (1,11):
    tree.insert(i)

tree.printInorder(tree.root)

print(f"Height= {tree.getHeight(tree.root)}")




        
    



