function TreeNode(value) {
    this.value = value;
    this.children = [];
}

function BinaryTreeNode(value) {
    this.value = value;
    this.left = null;
    this.right = null;
}

function BinaryTree() {
    this._root = null;
}

BinaryTree.prototype.traverseInOrder = function() {
    traverseInOrderHelper(this._root);

    function traverseInOrderHelper(node) {
        if (!node) {
            return;
        }
        traverseInOrderHelper(node.left);
        console.log(node.value);
        traverseInOrderHelper(node.right);
    }
}

BinaryTree.prototype.traverseInOrderIterative = function() {
    var current = this._root, s = [], done = false;

    while (!done) {
        if (current != null) {
            s.push(current);
            current = current.left
        } else {
            if (s.length) {
                current = s.pop();
                console.log(current.value);
                current = current.right;
            } else {
                done = true;
            }
        }
    }
}