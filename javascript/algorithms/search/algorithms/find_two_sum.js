// find two sums in linear time using memoization

function find_two_sum(array, sum) {
    let store = {};

    for (var i = 0, array_length = array.length; i < array_length; i++) {
        if (store[array[i]]) {
            return true;
        } else {
            store[sum - array[i]] = array[i];
        }
    }
    return false;
}