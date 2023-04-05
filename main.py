from RB_Tree import Tree

tree = Tree()




# for i in range(1, 11):
#     tree.insert(i)




# tree.printInorder(tree.root)


val=0

while val != 5:
    val = int(input("Enter 1 to insert word \nEnter 2 to Search for a word\nEnter 3 to find tree Height\nEnter 4 to find Dictionary Size\nEnter 5 to Quit\n"))
    if val==1:
        word = input("Enter Word to insert: ")
        tree.insert(word)
    elif val==2:
        word = input("Enter Word to Search for: ")
        if tree.search(tree.root,word):
            print("Word is Found")
        else:
            print("Word is not Found")
    elif val==3:
        print(f"Height= {tree.getHeight(tree.root)}")
    elif val==4:
        print(f"Dictionary Size = {tree.treeSize(tree.root)}")
    elif val==5:
        break
    else:
        print("Enter suitable number")