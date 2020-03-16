// O(n^2) bubble sort implementation

function swap(array, index1, index2) {
    let temp = array[index1];
    array[index1] = array[index2];
    array[index2] = temp;
}

function bubble_sort(array) {
    for (let i = 0; i < array.length; i++) {
        for (let j = 0; j <= i; j++) {
            if (array[i] < array[j]) {
                swap(array, i, j);
            }
        }
    }
    console.log(array);
    return array;
}

bubble_sort([6,3,2,1,4,5]); // [1,2,3,4,5,6]