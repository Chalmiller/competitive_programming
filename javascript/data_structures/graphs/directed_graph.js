function DirectedGraph() {
    this.edges = {};
}

DirectedGraph.prototype.addvertex = function(vertex) {
    this.edges[vertex] = {};
}

DirectedGraph.prototype.addEdge = function(origVertex, destVertex, weight) {
    if (weight === undefined) {
        weight = 0;
    }
    this.edges[origVertex][destVertex] = weight;
}

DirectedGraph.prototype.removeEdge = function(origVertex, destVertex) {
    if (this.edges[origVertex] && this.edges[origVertex][destVertex] != undefined) {
        delete this.edges[origVertex][destVertex];
    }
}

DirectedGraph.prototype.removeVertex = function(vertex) {
    for (var adjacentVertex in this.edges[vertex]) {
        this.removeEdge(adjacentVertex, vertex)
    }
    delete this.edges[vertex];
}

DirectedGraph.prototype.traverseBFS = function(vertex, fn) {
    var queue = [], visited = {};

    queue.push(vertex);

    while (queue.length) {
        vertex = queue.shift();
        if (!visited[vertex]) {
            visited[vertex] = true;
            fn(vertex);
            for (var adjacentVertex in this.edges[vertex]) {
                queue.push(adjacentVertex);
            }
        }
    }
}

DirectedGraph.prototype.traverseDFS = function(vertex, fn) {
    var visited = {};
    this._traverseDFS(vertex, visited, fn);
}

DirectedGraph.prototype._traverseDFS = function(vertex,visited, fn) {
    visited[vertex] = true;
    fn(vertex);
    for (var adjacentVertex in this.edges[vertex]) {
        if (!visited[adjacentVertex]) {
            this._traverseDFS(adjacentVertex, visited, fn);
        }
    }
}