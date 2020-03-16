// still O(n^2) time complexity and O(1) space complexity

function swap(array, index1, index2) {
    let temp = array[index1];
    array[index1] = array[index2];
    array[index2] = temp;
}

function selection_sort(items) {
    let len = items.length
    let min;

    for (let i = 0; i < len; i++) {
        min = i;
        for (let j = i+1; j < len; j++) {
            if (items[j] < items[min]) {
                min = j;
            }
        }

        if (i != min) {
            swap(items, i, min);
        }
    }
    console.log(items)
    return items;
}

selection_sort([6,1,23,4,2,3]); // [1, 2, 3, 4, 6, 23]