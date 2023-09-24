import assert from "assert";

class Node {
    right: Node | null = null;
    left: Node | null = null;
    value: number;

    constructor(value: number) {
        this.value = value;
    }
}

class BinarySearchTree {
    root: Node;

    constructor(value: number | Node) {
        if (typeof value === "number") {
            this.root = new Node(value);
        } else {
            this.root = value;
        }
    }

    insert(value: number, node: Node | null = null) {
        let _node = node === null ? this.root : node;
        if (_node.value > value) {
            if (_node.left === null) {
                _node.left = new Node(value);
            } else {
                // go to the left
                this.insert(value, _node.left);
            }
        } else if (_node.value < value) {
            if (_node.right === null) {
                _node.right = new Node(value);
            } else {
                // go to the right
                this.insert(value, _node.right);
            }
        }
    }

    getNodeHeight(value: number, node: Node | null = null) {
        let height = 0;
        let _node = node === null ? this.root : node;
        if (_node.value === value) {
            height = 0;
        }
        if (_node.value > value) {
            if (_node.left === null) {
                throw new Error();
            }
            // go to the left
            height = this.getNodeHeight(value, _node.left) + 1;
        } else if (_node.value < value) {
            if (_node.right === null) {
                throw new Error();
            }
            // go to the right
            height = this.getNodeHeight(value, _node.right) + 1;
        }
        return height;
    }
}

const binarySearchTree = new BinarySearchTree(50);

binarySearchTree.insert(30);
binarySearchTree.insert(70);
binarySearchTree.insert(40);
binarySearchTree.insert(60);
binarySearchTree.insert(20);
binarySearchTree.insert(80);

// 0 degree
assert.equal(binarySearchTree.root.value, 50);

// 1 degree
assert.equal((binarySearchTree.root.left as Node).value, 30);
assert.equal((binarySearchTree.root.right as Node).value, 70);

// 2 degree
assert.equal((binarySearchTree.root.left?.right as Node).value, 40);
assert.equal((binarySearchTree.root.left?.left as Node).value, 20);
assert.equal((binarySearchTree.root.right?.left as Node).value, 60);
assert.equal((binarySearchTree.root.right?.right as Node).value, 80);

// 0 degree
assert.equal(binarySearchTree.getNodeHeight(50), 0);

// 1 degree
assert.equal(binarySearchTree.getNodeHeight(30), 1);
assert.equal(binarySearchTree.getNodeHeight(30), 1);

// 2 degree
assert.equal(binarySearchTree.getNodeHeight(40), 2);
assert.equal(binarySearchTree.getNodeHeight(60), 2);
assert.equal(binarySearchTree.getNodeHeight(20), 2);
assert.equal(binarySearchTree.getNodeHeight(80), 2);

// inexistent node
assert.throws(() => binarySearchTree.getNodeHeight(-100), Error);

export default {};
