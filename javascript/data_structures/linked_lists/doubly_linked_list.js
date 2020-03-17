function DoublyLinkedListNode(data) {
    this.data = data;
    this.next = null;
    this.prev = null;
}

function DoublyLinkedList() {
    this.head = null;
    this.tail = null;
    this.size = 0;
}

DoublyLinkedList.prototype.isEmpty = function() {
    return this.size == 0;
}

DoublyLinkedList.prototype.addAtFront = function(value) {
    if (this.head === null) {
        this.head = new DoublyLinkedListNode(value);
        this.tail = this.head;
    } else {
        var temp = new DoublyLinkedListNode(value);
        temp.next = this.head;
        this.head.prev = temp;
        this.head = temp;
    }
    this.size++;
}

DoublyLinkedList.prototype.insertAtTail = function(value) {
    if (this.tail === null) {
        this.tail = new DoublyLinkedListNode(value);
        this.head = this.tail;
    } else {
        var temp = new DoublyLinkedListNode(value);
        temp.prev = this.tail;
        this.tail.next = temp;
        this.tail = temp;
    }
    this.size++;
}

DoublyLinkedList.prototype.deleteAtHead = function() {
    var toReturn = null;

    if (this.head !== null) {
        toReturn = this.head.data;

        if (this.tail === this.head) {
            this.head = null;
            this.tail = null;
        } else {
            this.head = this.head.next;
            this.head.prev = null;
        }
    }
    this.size--;
    return toReturn;
}

DoublyLinkedList.prototype.deleteAtTail = function() {
    var toReturn = null;

    if (this.tail !== null) {
        toReturn = this.tail.data;

        if (this.tail === this.head) {
            this.head = null;
            this.tail = null;
        } else {
            this.tail = this.tail.prev;
            this.tail.next = null;
        }
    }
    this.size--;
    return toReturn;
}

DoublyLinkedList.prototype.findStartingHead = function(value) {
    var currentHead = this.head;
    while(currentHead.next) {
        if (currentHead.data == value) {
            return true;
        }
        currentHead = currentHead.next;
    }
    return false;
}

DoublyLinkedList.prototype.findStartingTail = function(value) {
    var currentTail = this.tail;
    while(currentTail.prev) {
        if (currentTail.data == value) {
            return true;
        }
        currentTail = currentTail.prev;
    }
    return false;
}