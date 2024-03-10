def find_max_value(node):
    if not node:
        return
    current_node = node
    while current_node.right is not None:
        current_node = current_node.right
    return current_node.key


def find_min_value(node):
    if not node:
        return
    current_node = node
    while current_node.left is not None:
        current_node = current_node.left
    return current_node.key


def find_sum_of_nodes(node):
    if not node:
        return 0
    interm_sum = node.key
    right_sum = find_sum_of_nodes(node.right)
    left_sum = find_sum_of_nodes(node.left)
    interm_sum = interm_sum + left_sum + right_sum

    return interm_sum


if __name__ == "__main__":
    from avl_tree import AVLNode, insert, delete_node
    # Driver program to test the above functions
    root = None
    print(root)
    print("Мінімальне значення: ", find_min_value(root))
    print("Максимальне значення: ", find_max_value(root))
    print("Сума: ", find_sum_of_nodes(root))
    print("*" * 20)

    keys = [10, 20, 30, 25, 28, 27, -1]

    for key in keys:
        root = insert(root, key)
        print("Вставлено:", key)
        print("AVL-Дерево:")
        print(root)
        print("Мінімальне значення: ", find_min_value(root))
        print("Максимальне значення: ", find_max_value(root))
        print("Сума: ", find_sum_of_nodes(root))
        print("*"*20)

    # Delete
    keys_to_delete = [10, 27]
    for key in keys_to_delete:
        root = delete_node(root, key)
        print("Видалено:", key)
        print("AVL-Дерево:")
        print(root)
        print("Мінімальне значення: ", find_min_value(root))
        print("Максимальне значення: ", find_max_value(root))
        print("Сума: ", find_sum_of_nodes(root))
        print("*"*20)
