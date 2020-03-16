function binary_search(array, n) {
    var lowIndex = 0, highIndex = array.length-1;

    while(lowIndex <= highIndex) {
        var midIndex = Math.floor((highIndex + lowIndex) / 2);
        if (array[midIndex] == n) {
            return midIndex;
        } else if (n > array[midIndex]){
            lowIndex = midIndex;
        } else {
            highIndex = midIndex;
        }
    }
    return -1;
}

function recursive_binary_search(array, n, low, high) {
    let mid = (low+high)/2
    if (array[mid] == n) {
        return true;
    } else if (n > array[mid]) {
        return recursive_binary_search(array, n, mid, high);
    } else {
        return recursive_binary_search(array, n, low, mid-1);
    }
}