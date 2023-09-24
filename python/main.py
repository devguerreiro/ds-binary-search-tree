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

    def search(self, value: int, node: Node | None = None):
        node = self.root if node is None else node
        if node.value == value:
            return 0
        elif node.value > value:
            if node.left is None:
                raise ValueError()
            # go to the left
            height = self.search(value, node.left) + 1
        elif node.value < value:
            if node.right is None:
                raise ValueError()
            # go to the right
            height = self.search(value, node.right) + 1
        return height


if __name__ == "__main__":
    binary_search_tree = BinarySearchTree(50)

    binary_search_tree.add(30)
    binary_search_tree.add(70)
    binary_search_tree.add(40)
    binary_search_tree.add(60)
    binary_search_tree.add(20)
    binary_search_tree.add(80)

    # 0 degree
    assert binary_search_tree.root.value == 50

    # 1 degree
    assert binary_search_tree.root.left.value == 30
    assert binary_search_tree.root.right.value == 70

    # 2 degree
    assert binary_search_tree.root.left.right.value == 40
    assert binary_search_tree.root.left.left.value == 20
    assert binary_search_tree.root.right.left.value == 60
    assert binary_search_tree.root.right.right.value == 80

    # 0 degree
    assert binary_search_tree.search(50) == 0

    # 1 degree
    assert binary_search_tree.search(30) == 1
    assert binary_search_tree.search(70) == 1

    # 2 degree
    assert binary_search_tree.search(40) == 2
    assert binary_search_tree.search(60) == 2
    assert binary_search_tree.search(20) == 2
    assert binary_search_tree.search(80) == 2

    # inexistent value
    try:
        binary_search_tree.search(-100)
        raise AssertionError()
    except Exception as e:
        assert isinstance(e, ValueError)
