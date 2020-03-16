// Time complexity O(n)

function linearSearch(array, n) {
    for (var i=0; i <array.length; i++) {
        if (array[i] == n) {return true;}
    }
    return false;
}