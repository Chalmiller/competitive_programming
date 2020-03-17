function Customer(name, order) {
    this.name = name;
    this.order = order;
}

function Cashier() {
    this.customers = new Queue();
}

Cashier.prototype.addOrder = function (customer) {
    this.customers.enqueue(customer);
}

Cashier.prototype.deliverOrder = function() {
    var finishedCustomer = this.customers.dequeue();

    console.log(finishedCustomer.name + ", your " + finishedCustomer.order + " is ready!")
}