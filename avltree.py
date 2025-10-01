class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # Height of node for balancing

def getHeight(node):
    if not node:
        return 0
    return node.height

def getBalance(node):
    if not node:
        return 0
    return getHeight(node.left) - getHeight(node.right)

def rightRotate(y):
    x = y.left
    T2 = x.right

    #perform rotation
    x.right = y
    y.left = T2

    y.height = 1 + max(getHeight(y.left), getHeight(y.right))
    x.height = 1 + max(getHeight(x.left), getHeight(x.right))
    
    #new root
    return x

def leftRotate(x):
    y = x.right
    T2 = y.left

    #perform rotation 
    y.left = x
    x.right = T2

    y.height = 1 + max(getHeight(y.left), getHeight(y.right))
    x.height = 1 + max(getHeight(x.left), getHeight(x.right))

    #new root
    return y

def insert(node, key):
    #1. Perform the normal BST insert
    if not node:
        return Node(key)
    elif key<node.key:
        node.left = insert(node.left, key)
    elif key>node.key:
        node.right = insert(node.right, key)
    else:
        return node  # Duplicate keys are not allowed in the AVL tree
    
    #2. Update height of this ancestor node
    node.height = 1 + max(getHeight(node.left), getHeight(node.right))

    balance = getBalance(node)

    #3. If the node becomes unbalanced, then there are 4 cases
    #Left Left Case
    if balance > 1 and key < node.left.key:
        return rightRotate(node)
    
    #Right Right Case
    if balance < -1 and key > node.right.key:
        return leftRotate(node)
    
    #Left Right Case
    if balance > 1 and key > node.left.key:
        node.left = leftRotate(node.left)
        return rightRotate(node)
    
    #Right Left Case
    if balance < -1 and key < node.right.key:
        node.right = rightRotate(node.right)
        return leftRotate(node)
    
    return node

def preOrder(node):
    if not node:
        return
    print("{0} ".format(node.key), end="")
    preOrder(node.left)
    preOrder(node.right)

def search(node, key):
    #Base Cases: root is null or key is present at root
    if node is None or node.key == key:
        return node
    
    #Key is greater than root's key
    if key > node.key:
        return search(node.right, key)
    
    #Key is smaller than root's key
    return search(node.left, key)

def minValueNode(node):
    current = node

    #loop down to find the leftmost leaf
    while current.left is not None:
        current = current.left
    
    return current


def delete(node, key):
    #STEP 1: PERFORM STANDARD BST DELETE
    if not node:
        return node
    
    elif key < node.key:
        node.left = delete(node.left, key)
    
    elif key > node.key:
        node.right = delete(node.right, key)
    
    else:
        #Node with only one child or no child
        if node.left is None:
            temp = node.right
            node = None
            return temp
        elif node.right is None:
            temp = node.left
            node = None
            return temp
        
        #Node with two children: Get the inorder successor (smallest in the right subtree)
        temp = minValueNode(node.right)

        #Copy the inorder successor's content to this node
        node.key = temp.key

        #Delete the inorder successor
        node.right = delete(node.right, temp.key)
    
    #If the tree had only one node then return
    if node is None:
        return node
    
    #STEP 2: UPDATE THE HEIGHT OF THE CURRENT NODE
    node.height = 1 + max(getHeight(node.left), getHeight(node.right))

    #STEP 3: GET THE BALANCE FACTOR OF THIS NODE (to check whether this node became unbalanced)
    balance = getBalance(node)

    #If this node becomes unbalanced, then there are 4 cases

    #Left Left Case
    if balance > 1 and getBalance(node.left) >= 0:
        return rightRotate(node)
    
    #Left Right Case
    if balance > 1 and getBalance(node.left) < 0:
        node.left = leftRotate(node.left)
        return rightRotate(node)
    
    #Right Right Case
    if balance < -1 and getBalance(node.right) <= 0:
        return leftRotate(node)
    
    #Right Left Case
    if balance < -1 and getBalance(node.right) > 0:
        node.right = rightRotate(node.right)
        return leftRotate(node)
    
    return node
    
    
