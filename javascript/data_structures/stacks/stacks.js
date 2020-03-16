function Stack(array) {
    this.array = [];
    if(array) this.array = array;
}

Stack.prototype.getBuffer = function() {
    return this.array.slice();
}

Stack.prototype.isEmpty = function() {
    return this.array.length == 0;
}

Stack.prototype.push = function() {
    this.array.push(value)
}

Stack.prototype.peek = function() {
    return this.array[this.array.length-1];
}

Stack.prototype.pop = function() {
    return this.array.pop();
}

function stackAccessNthTopNode(stack, n) {
    var bufferArray = stack.getBuffer();
    if (n <= 0) throw 'error';

    var bufferStack = new Stack(bufferArray);

    while (--n !== 0) {
        bufferStack.pop();
    }
    return bufferStack.pop()
}

function stackSearch(stack, element) {
    var bufferArray = stack.getBuffer();

    var bufferStack = new Stack(bufferArray);

    while (!bufferStack.isEmpty()) {
        if (bufferStack.pop() == element) {
            return true;
        }
    }
    return false;
}

var stack1 = new Stack();
