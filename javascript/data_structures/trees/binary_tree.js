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