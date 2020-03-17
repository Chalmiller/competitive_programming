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

BinaryTree.prototype.traverseLevelOrder = function() {
    var root = this._root, queue = [];

    if (!root) return;
    queue.push(root);

    while (queue.length) {
        var temp = queue.shift();
        console.log(temp.value);
        if (temp.left) queue.push(temp.left);
        if (temp.right) queue.push(temp.right);
    }
}