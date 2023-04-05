from RB_Tree import Tree

tree = Tree()
for i in range(1, 11):
    tree.insert(i)


if tree.search(tree.root,2):
    print("Main Found")



# tree.printInorder(tree.root)
#
# print(f"Height= {tree.getHeight(tree.root)}")
#
# tree.search(tree.root,9)
#
# print(tree.treeSize(tree.root))