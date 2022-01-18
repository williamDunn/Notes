# Tree 101
-----------

First, create a node class that will represent a node in a tree

```
class Node {
    int value;
    Node left;
    Node right;
 
    public Node(int value) {
        this.value = value;
    }
}
```

## Common Operations:

#### Insertion:

```
public void add(int value) {
    root = add(root, value);
}
 
private Node add(Node current, int value) {
 
    if (current == null) {
        return new Node(value);
    }
 
    if (value < current.value) {
        current.left= add(current.left, value);
    } else if (value > current.value) {
        current.right = add(current.right, value);
    }
 
    return current;
}
```


#### Deletion:


```
public void delete(int value) {
        root = delete(root, value);
    }
 
    private Node delete(Node current, int value) {
        if (current == null) {
            return null;
        }
 
        if (value == current.value) {
            // No children
            if (current.left == null && current.right == null) {
                return null;
            }
 
            // Only 1 child
            if (current.right == null) {
                return current.left;
            }
            if (current.left == null) {
                return current.right;
            }
 
            // Two children
            int smallestValue = findSmallestValue(current.right);
            current.value = smallestValue;
            current.right = delete(current.right, smallestValue);
            return current;
        }
        if (value < current.value) {
            current.left = delete(current.left, value);
            return current;
        }
 
        current.right = delete(current.right, value);
        return current;
    }
```

#### Searching

```
public boolean containsNode(int value) {
    return containsNode(root, value);
}
 
private boolean containsNode(Node current, int value) {
    if (current == null) {
        return false;
    }
 
    if (value == current.value) {
        return true;
    }
 
    return value < current.value
            ? containsNode(current.left, value)
            : containsNode(current.right, value);
}
```

## Traversing - O(n)

### DFS in-order
-  The in-order traversal consists of first visiting the left sub-tree, then the root node, and finally the right sub-tree
-  In the case of binary search trees (BST), Inorder traversal gives nodes in non-decreasing order. To get nodes of BST in non-increasing order, a variation of Inorder traversal where Inorder traversal s reversed can be used. 
```
public void inOrderTraversal(Node node) {
    if (node != null) {
        inOrderTraversal(node.left);
        print(node.value);
        inOrderTraversal(node.right);
    }
}
```

### DFS pre-order
-  Pre-order traversal visits first the root node, then the left subtree, and finally the right subtree
-  Preorder traversal is used to create a copy of the tree

```
public void preOrderTraversal(Node node) {
    if (node != null) {
        print(node.value);
        preOrderTraversal(node.left);
        preOrderTraversal(node.right);
    }
}
```

### DFS post-order
-  Post-order traversal visits the left subtree, the right subtree, and the root node at the end
-  Postorder traversal is used to delete the tree.

```
public void postOrderTraversal(Node node) {
    if (node != null) {
        postOrderTraversal(node.left);
        postOrderTraversal(node.right);
        print(node.value);
    }
}
```

