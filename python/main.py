from typing import TypeVar


TNode = TypeVar("TNode", bound="Node")


class Node:
    right: TNode | None = None
    left: TNode | None = None
    value: int

    def __init__(self, value: int):
        self.value = value


class BinarySearchTree:
    root: Node

    def __init__(self, value: int):
        self.root = Node(value)

    def add(self, value: int, node: Node | None = None):
        node = self.root if node is None else node
        if node.value > value:
            if node.left is None:
                node.left = Node(value)
            else:
                # go to the left
                self.add(value, node.left)
        elif node.value < value:
            if node.right is None:
                node.right = Node(value)
            else:
                # go to the right
                self.add(value, node.right)
        return


if __name__ == "__main__":
    binary_search_tree = BinarySearchTree(50)

    binary_search_tree.add(30)
    binary_search_tree.add(70)
    binary_search_tree.add(40)
    binary_search_tree.add(60)
    binary_search_tree.add(20)
    binary_search_tree.add(80)

    assert binary_search_tree.root.value == 50

    assert binary_search_tree.root.left.value == 30
    assert binary_search_tree.root.left.right.value == 40
    assert binary_search_tree.root.left.left.value == 20

    assert binary_search_tree.root.right.value == 70
    assert binary_search_tree.root.right.left.value == 60
    assert binary_search_tree.root.right.right.value == 80
