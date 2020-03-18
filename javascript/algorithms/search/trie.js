function TrieNode() {
    this.children = {};
    this.endOfWord = false;
}

function Trie() {
    this.root = new TrieNode();
}

Trie.prototype.insert = function(word) {
    var current = this.root;
    for (var i = 0; i < word.length; i++) {
        var ch = word.charAt(i);
        var node = current.children[ch];
        if (node == null) {
            node = new TrieNode();
            current.children[ch] = node;
        }
        current = node;
    }
    current.endOfWord = true;
}

Trie.prototype.search = function(word) {
    var current = this.root;
    for (var i = 0; i < word.length; i++) {
        var ch = word.charAt(i);
        var node = current.children[ch];
        if (node == null) {
            return false
        }
        current = node;
    }
    return current.endOfWord;
}

Trie.prototype.delete = function(word) {
    this.deleteRecursively(this.root, word, 0);
}

Trie.prototype.deleteRecursively = function(current, word, index) {
    if (index == word.length) {
        if (!current.endOfWord) {
            return false;
        }
        current.endOfWord = false;
        return Object.keys(current.children).length == 0;
    }
    var ch = word.charAt(index), node = current.children[ch];
    if (node == null) {
        return false;
    }
    var shouldDeleteCurrentNode = this.deleteRecursively(node, word, index + 1);

    if (shouldDeleteCurrentNode) {
        delete current.children[ch];
        return Object.keys(current.children).length == 0;
    }
    return false;
}