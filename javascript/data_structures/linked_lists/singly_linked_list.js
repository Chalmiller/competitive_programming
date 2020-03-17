function SinglyLinkedListNode(data) {
    this.data = data;
    this.next = null;
}

function SinglyLinkedList() {
    this.head = null;
    this.size = 0;
}

SinglyLinkedList.prototype.isEmpty = function() {
    return this.size == 0;
}

SinglyLinkedList.prototype.insert = function(value) {
    if (this.head === null) {
        this.head = new SinglyLinkedListNode(value);
    } else {
        var temp = this.head;
        this.head = new SinglyLinkedListNode(value);
        this.head.next = temp;
    }
    this.size++;
}

SinglyLinkedList.prototype.remove = function(value) {
    var currentHead = this.head;
    if (currentHead.data == value) {
        this.head = currentHead.next;
        this.size--;
    } else {
        var prev = currentHead;
        while(currentHead.next) {
            if (currentHead.data == value) {
                prev.next = currentHead.next;
                prev = currentHead;
                currentHead = currentHead.next;
                break;
            }
            prev = currentHead;
            currentHead = currentHead.next;
        }
        if (currentHead.data == value) {
            prev.next = null;
        }
        this.size--;
    }
}

SinglyLinkedList.prototype.find = function(value) {
    var currentHead = this.head;
    while (currentHead.next) {
        if (currentHead.data == value) {
            return true;
        }
        currentHead = currentHead.next;
    }
    return false;
}