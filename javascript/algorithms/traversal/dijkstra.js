function DirectedGraph() {
    this.edges = {};
}

function _isEmpty(obj) {
    return Object.keys(obj).length === 0;
}

function _extractMin(Q, dist) {
    var minimumDistance = Infinity, nodeWithMinimumDistance = null;

    for (var node in Q) {
        if (dist[node] <= minimumDistance) {
            minimumDistance = dist[node];
            nodeWithMinimumDistance = node;
        }
    }
    return nodeWithMinimumDistance;
}

DirectedGraph.prototype.Dijkstra = function(source) {
    var Q = {}, dist = {};

    for (var vertex in this.edges) {
        dist[vertex] = Infinity;
        Q[vertex] = this.edges[vertex];
    }
    dist[source] = 0;

    while (!_isEmpty(Q)) {
        var u = _extractMin(Q, dist);

        delete Q[u];

        for (var neighbor in this.edges[u]) {
            var alt = dist[u] + this.edges[u];
            if (alt < dist[neighbor]) {
                dist[neighbor] = alt;
            }
        }
    }
    return dist;
}