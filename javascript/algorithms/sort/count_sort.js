function count_sort(array) {
    let hash = {}, count_array = [];
    for (let i = 0; i < array.length; i++) {
        if (!hash[array[i]]) {
            hash[array[i]] = 1;
        } else {
            hash[array[i]]++;
        }
    }

    for (var key in hash) {
        for (var i = 0; i < hash[key]; i++) {
            count_array.push(parseInt(key));
        }
    }

    return count_array;
}