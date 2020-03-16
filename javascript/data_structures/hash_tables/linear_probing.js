function hash_table(size) {
    this.size = size;
    this.keys = this.initArray(size);
    this.values = this.initArray(size);
    this.limit = 0;
}

hash_table.prototype.put = function(key, value) {
    if (this.limit >= this.size) throw 'hash table is full';

    var hashed_index = this.hash(key);

    while (this.keys[hashed_index] != null) {
        hashed_index++;
        hashed_index = hashed_index % this.size;
    }

    this.keys[hashed_index] = key;
    this.values[hashed_index] = value;
    this.limit++;
}

hash_table.prototype.get = function(key) {
    var hashed_index = this.hash(key);

    while (this.keys[hashed_index] != key) {
        hashed_index++;
        hashed_index = hashed_index % this.size;
    }
    return this.values[hashed_index];
}

hash_table.prototype.hash = function(key) {
    if (!Number.isInteger(key)) throw 'must be int';
    return key % this.size;
}

hash_table.prototype.initArray = function (size) {
    var array = [];
    for (var i = 0; i < size; i++) {
        array.push(null);
    }
    return array;
}

var example_table = new hash_table(13);
example_table.put(7, 'hi');
example_table.put(20, 'hello');
example_table.put(33, 'sunny');
example_table.put(46, 'weather');
example_table.put(59, 'wow');
example_table.put(72, 'forty');
example_table.put(85, 'happy');
example_table.put(98, 'sad');

console.log(hash_table);
