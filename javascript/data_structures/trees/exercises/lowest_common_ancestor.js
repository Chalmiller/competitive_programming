function findLowestCommonAncestor(root, value1, value2) {
    function findLowestCommonAncestorHelper(root, value1, value2) {
        if (!root) return;
        if (Math.max(value1, value2) < root.value) {
            return findLowestCommonAncestorHelper(root.left, value1, value2)
        }
        if (Math.max(value1, value2) > root.value) {
            return findLowestCommonAncestorHelper(root.right, value1, value2)
        }
        return root.value;
    }
    return findLowestCommonAncestorHelper(root, value1, value2);
}