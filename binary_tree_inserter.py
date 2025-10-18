class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def display_tree(node, level=0, prefix="Root: "):
    """Recursively print the binary tree in a readable format."""
    if node is not None:
        print(" " * (level * 4) + prefix + str(node.data))
        if node.left or node.right:
            display_tree(node.left, level + 1, "L--- ")
            display_tree(node.right, level + 1, "R--- ")


def find_node(node, value):
    """Search for a node by its data value."""
    if node is None:
        return None
    if node.data == value:
        return node
    # Search left and right subtrees
    found = find_node(node.left, value)
    if found:
        return found
    return find_node(node.right, value)


def main():
    print("\nBinary Tree Builder")
    root_val = input("Enter value for root node: ").strip()
    root = TreeNode(root_val)
    print(f"Root '{root_val}' created.\n")

    while True:
        display_tree(root)
        print("\nDo you want to add more nodes? (y/n)")
        choice = input("Enter choice: ").strip().lower()
        if choice == "n":
            print("\nFinal Tree Structure:\n")
            display_tree(root)
            print("\nProgram finished.")
            break

        # Ask which node to add children to
        parent_val = input("Enter the value of the parent node: ").strip()
        parent = find_node(root, parent_val)

        if not parent:
            print(f"Node '{parent_val}' not found! Try again.\n")
            continue

        # Choose to add left or right child
        print("\nDo you want to add a:")
        print("1. Left child")
        print("2. Right child")
        side = input("Enter 1 or 2: ").strip()

        if side == "1":
            if parent.left is not None:
                print(f"'{parent_val}' already has a left child ({parent.left.data}).")
            else:
                new_val = input(f"Enter value for left child of '{parent_val}': ").strip()
                parent.left = TreeNode(new_val)
                print(f"Added '{new_val}' as left child of '{parent_val}'.\n")

        elif side == "2":
            if parent.right is not None:
                print(f"'{parent_val}' already has a right child ({parent.right.data}).")
            else:
                new_val = input(f"Enter value for right child of '{parent_val}': ").strip()
                parent.right = TreeNode(new_val)
                print(f"Added '{new_val}' as right child of '{parent_val}'.\n")

        else:
            print("Invalid input. Please enter 1 or 2.\n")


if __name__ == "__main__":
    main()
