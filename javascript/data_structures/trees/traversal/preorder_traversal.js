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

BinaryTree.prototype.traversePreOrder = function() {
    traversePreOrderHelper(this._root);

    function traversePreOrderHelper(node) {
        if (!node) return;
        console.log(node.value);
        traversePreOrderHelper(node.left);
        traversePreOrderHelper(node.right);
    }
}

BinaryTree.prototype.traversePreOrderIterative = function() {
    var nodeStack = [];
    nodeStack.push(this._root);

    while (nodeStack.length) {
        var node = nodeStack.pop();
        console.log(node.value);

        if (node.right) {
            nodeStack.push(node.right);
        }
        if (node.left) {
            nodeStack.push(node.left);
        }
    }
}