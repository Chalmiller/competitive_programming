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