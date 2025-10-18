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


def display_tree(root):
    """Display the binary tree in a structured left-right format (graphical style)."""
    if not root:
        print("(empty tree)")
        return

    lines, *_ = build_tree_string(root, 0, False, '-')
    for line in lines:
        print(line)


def build_tree_string(root, curr_index, include_index=False, delimiter='-'):
    """Recursively build a printable tree structure (ASCII art style)."""
    if root is None:
        return [], 0, 0, 0

    line1 = []
    line2 = []

    node_repr = str(root.data)

    new_root_width = gap_size = len(node_repr)

    # Get the left and right sub-boxes, their widths, and root start/end positions
    l_box, l_box_width, l_root_start, l_root_end = build_tree_string(root.left, 2 * curr_index + 1, include_index, delimiter)
    r_box, r_box_width, r_root_start, r_root_end = build_tree_string(root.right, 2 * curr_index + 2, include_index, delimiter)

    # Draw branches connecting the current node to its children
    if l_box_width > 0:
        l_root = (l_root_start + l_root_end) // 2 + 1
        line1.append(' ' * (l_root + 1))
        line1.append('_' * (l_box_width - l_root))
        line2.append(' ' * l_root + '/')
        line2.append(' ' * (l_box_width - l_root))
        new_root_start = l_box_width + 1
    else:
        new_root_start = 0

    line1.append(node_repr)
    line2.append(' ' * new_root_width)

    if r_box_width > 0:
        r_root = (r_root_start + r_root_end) // 2
        line1.append('_' * r_root)
        line1.append(' ' * (r_box_width - r_root))
        line2.append(' ' * r_root + '\\')
        line2.append(' ' * (r_box_width - r_root))

    gap = ' '
    new_root_end = new_root_start + new_root_width - 1
    gap_size = 1

    new_box = [''.join(line1), ''.join(line2)]

    # Merge sub-boxes with spaces in between
    l_box_height = len(l_box)
    r_box_height = len(r_box)
    max_box_height = max(l_box_height, r_box_height)
    for i in range(max_box_height):
        left_line = l_box[i] if i < l_box_height else ' ' * l_box_width
        right_line = r_box[i] if i < r_box_height else ' ' * r_box_width
        new_box.append(left_line + gap * gap_size + right_line)

    return new_box, len(new_box[0]), new_root_start, new_root_end


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
