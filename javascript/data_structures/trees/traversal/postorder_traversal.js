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

BinaryTree.prototype.traversePostOrder = function() {
    traversePostOrderHelper(this._root);

    function traversePostOrderHelper(node) {
        if (node.left) traversePostOrderHelper(node.left);
        if (node.right) traversePostOrderHelper(node.right);
        console.log(node.value);
    }
}

BinaryTree.prototype.traversePostOrderIterative = function() {
    var s1 = [], s2 = [];
    s1.push(this._root);

    while (s1.length) {
        var node = s1.pop();
        s2.push(node);

        if (node.left) s1.push(node.left);
        if (node.right) s1.push(node.right);
    }

    while(s2.length) {
        var node = s2.pop();
        console.log(node.value);
    }
}