function DirectedGraph() {
    this.edges = {};
}

DirectedGraph.prototype.topologicalSortUtil = function(v, visited, stack) {
    visited.add(v);

    for (var item in this.edges[v]) {
        if (visited.has(item) == false) {
            this.topologicalSortUtil(item, visited, stack)
        }
    }
    stack.unshift(v);
};

DirectedGraph.prototype.topologicalSort = function() {
    var visited = {}, stack = [];

    for (var item in this.edges) {
        if (visited.has(item) == false) {
            this.topologicalSortUtil(item, visited, stack);
        }
    }
    return stack;
};

