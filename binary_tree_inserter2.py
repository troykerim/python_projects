class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def find_node(node, value):
    """Search for a node by its data value."""
    if node is None:
        return None
    if node.data == value:
        return node
    found = find_node(node.left, value)
    if found:
        return found
    return find_node(node.right, value)


def get_tree_depth(root):
    if not root:
        return 0
    return 1 + max(get_tree_depth(root.left), get_tree_depth(root.right))


def display_tree(root):
    """Prints the binary tree with consistent spacing."""
    if root is None:
        print("(empty tree)")
        return

    depth = get_tree_depth(root)
    max_width = 2 ** depth * 4

    def fill_levels(node, level=0, pos=max_width // 2, result=None):
        if result is None:
            result = {}
        if node is None:
            return result
        if level not in result:
            result[level] = []
        result[level].append((pos, str(node.data)))
        gap = max_width // (2 ** (level + 2))
        fill_levels(node.left, level + 1, pos - gap, result)
        fill_levels(node.right, level + 1, pos + gap, result)
        return result

    levels = fill_levels(root)
    last_line = 0
    for level in sorted(levels.keys()):
        line = ""
        prev_pos = 0
        for pos, val in sorted(levels[level], key=lambda x: x[0]):
            space = pos - prev_pos
            line += " " * max(space, 0) + val
            prev_pos = pos + len(val)
        print(line.rstrip())
        last_line = level


def main():
    print("\nBinary Tree Builder")
    root_val = input("Enter value for root node: ").strip()
    root = TreeNode(root_val)
    print(f"Root '{root_val}' created.\n")

    while True:
        print("\nCurrent Tree Structure:\n")
        display_tree(root)
        print("\nDo you want to add more nodes? (y/n)")
        choice = input("Enter choice: ").strip().lower()
        if choice == "n":
            print("\nFinal Tree Structure:\n")
            display_tree(root)
            print("\nProgram finished.")
            break

        parent_val = input("Enter the value of the parent node: ").strip()
        parent = find_node(root, parent_val)

        if not parent:
            print(f"Node '{parent_val}' not found! Try again.\n")
            continue

        print("\nDo you want to add a:")
        print("1. Left child")
        print("2. Right child")
        side = input("Enter 1 or 2: ").strip()

        if side == "1":
            if parent.left:
                print(f"'{parent_val}' already has a left child ({parent.left.data}).")
            else:
                new_val = input(f"Enter value for left child of '{parent_val}': ").strip()
                parent.left = TreeNode(new_val)
                print(f"Added '{new_val}' as left child of '{parent_val}'.\n")

        elif side == "2":
            if parent.right:
                print(f"'{parent_val}' already has a right child ({parent.right.data}).")
            else:
                new_val = input(f"Enter value for right child of '{parent_val}': ").strip()
                parent.right = TreeNode(new_val)
                print(f"Added '{new_val}' as right child of '{parent_val}'.\n")

        else:
            print("Invalid input. Please enter 1 or 2.\n")


if __name__ == "__main__":
    main()
