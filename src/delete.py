# DELETE

# - Find the node
# - Compare target to current value
    # If target is less than, go left, -> set current = left child
    # If target is greater than, go right -> set current = right child
    # Repeat until target == current value
    # OR we don't find it

# - If we don't find it - we return None
# - If we do find it - current == target
    # - Find the replacement: to go the left most child on the right subtree
# How do we traverse through nodes to find the next greatest value
    # - While replacement has a left child: replacement = replacement.left
    # - Replacement's parent.left = None
    # - Target's parent(left or right) = replacement
        # - Need to keep tract of targets parent
        # - And if it's the left or right subschild
    # - Replacement.left = target.left
    # - Replacement.right = target.right

def delete(self,target):
    target_node = self
    parent_node = None
    while True:
    if target < self.value:
        parent_node = current
        current = current.left
    elif target > current.value
        parent_node = current
        current = current.right
    else:
        target_node = current
        break

    replacement_parent_node = None
    replacement = None
    current = target_node.right
    while True:
        if current.left is None:
            replacement = current
            break
        else:
            replacement_parent_node = current
            current = current.left

    replacement_parent_node = None

    if target_node.value < parent_node.value:
        parent_node.left = replacement
    else:
        # Target node value > parent node value, it's the right child
        # parent_node.right = replacement

    replacement.left = target_node.left_child
    replacement.right = 
    
def find_minimum_value(self):
    # While current has left child: replacement = replacement.left
    # Recursive
    # base case:
    if self.left is None:
        return self
    left_child = self.left
    min = left_child.find_minimum_value()
    return min

class BST:

    def find_minimum_value(self):
        return self.root.find_minimum_value()