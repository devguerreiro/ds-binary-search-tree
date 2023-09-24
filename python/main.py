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

    def __init__(self, value: int | None = None, node: Node | None = None):
        if node is not None:
            self.root = node
        elif value is not None:
            self.root = Node(value)

    def insert(self, value: int, node: Node | None = None):
        _node = self.root if node is None else node
        if _node.value > value:
            if _node.left is None:
                _node.left = Node(value)
            else:
                # go to the left
                self.insert(value, _node.left)
        elif _node.value < value:
            if _node.right is None:
                _node.right = Node(value)
            else:
                # go to the right
                self.insert(value, _node.right)
        return

    def get_node_height(self, value: int, node: Node | None = None):
        _node = self.root if node is None else node
        if _node.value == value:
            return 0
        elif _node.value > value:
            if _node.left is None:
                raise ValueError()
            # go to the left
            height = self.get_node_height(value, _node.left) + 1
        elif _node.value < value:
            if _node.right is None:
                raise ValueError()
            # go to the right
            height = self.get_node_height(value, _node.right) + 1
        return height

    def search(self, value: int, node: Node | None = None):
        _node = self.root if node is None else node
        if _node.value == value:
            return BinarySearchTree(node=_node)
        elif _node.value > value:
            if _node.left is None:
                raise ValueError()
            # go to the left
            return self.search(value, _node.left)
        if _node.right is None:
            raise ValueError()
        # go to the right
        return self.search(value, _node.right)

    def height_traversal(self, node: Node | None = None):
        pass


if __name__ == "__main__":
    binary_search_tree = BinarySearchTree(50)

    binary_search_tree.insert(30)
    binary_search_tree.insert(70)
    binary_search_tree.insert(40)
    binary_search_tree.insert(60)
    binary_search_tree.insert(20)
    binary_search_tree.insert(80)

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
    assert binary_search_tree.get_node_height(50) == 0

    # 1 degree
    assert binary_search_tree.get_node_height(30) == 1
    assert binary_search_tree.get_node_height(70) == 1

    # 2 degree
    assert binary_search_tree.get_node_height(40) == 2
    assert binary_search_tree.get_node_height(60) == 2
    assert binary_search_tree.get_node_height(20) == 2
    assert binary_search_tree.get_node_height(80) == 2

    # inexistent node
    try:
        binary_search_tree.get_node_height(-100)
        raise AssertionError()
    except Exception as e:
        assert isinstance(e, ValueError)

    # search subtree
    assert isinstance(binary_search_tree.search(30), BinarySearchTree)

    sub_binary_search_tree = binary_search_tree.search(30)

    # 0 degree
    assert sub_binary_search_tree.root.value == 30

    # 1 degree
    assert sub_binary_search_tree.root.left.value == 20
    assert sub_binary_search_tree.root.right.value == 40

    # inexistent node
    try:
        binary_search_tree.search(-100)
        raise AssertionError()
    except Exception as e:
        assert isinstance(e, ValueError)
