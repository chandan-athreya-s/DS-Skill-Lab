# Python program to delete nodes 
# which have a greater value on
# right side

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# This function deletes nodes on the 
# right side of the linked list
def delete_nodes(node):
    
    # If next is NULL, then there is no node 
    # with greater value on right side.
    if node is None or node.next is None:
        return node
    
    # find the next node using recursion
    # It will return the node with the 
    # greatest value on right side.
    next_node = delete_nodes(node.next)
    
    # if right node's value is greater than
    # current node's value, then we can simply 
    # return the next node
    if next_node.data > node.data:
        return next_node
    
    # if current node's value is greater, then
    # point it to the next node, and return the
      # the current node.
    node.next = next_node
    return node

def print_list(curr):
    while curr is not None:
        print(f" {curr.data}", end="")
        curr = curr.next
    print()

if __name__ == "__main__":
    
    # Create a hard-coded linked list:
    # 12 -> 15 -> 10 -> 11 -> 5 -> 6 -> 2 -> 3
    head = Node(12)
    head.next = Node(15)
    head.next.next = Node(10)
    head.next.next.next = Node(11)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(2)
    head.next.next.next.next.next.next.next = Node(3)

    head = delete_nodes(head)

    print_list(head)
