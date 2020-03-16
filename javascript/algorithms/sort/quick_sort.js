function quick_sort(items) {
    return quick_sort_helper(items, 0, items.length - 1);
}

function quick_sort_helper(items, left, right) {
    let index;
    if (items.length > 1) {
        index = partition(items, left, right);

        if (left < index - 1) {
            quick_sort_helper(items, left, index - 1);
        }

        if (index < right) {
            quick_sort_helper(items, index, right);
        }
    }
    console.log(items);
    return items;
}

function partition(array, left, right) {
    var pivot = array[Math.floor((right + left) / 2)];
    while(left <= right) {
        while(pivot > array[left]) {
            left++;
        }
        while (pivot < array[right]) {
            right--;
        }
        if (left <= right) {
            let temp = array[left];
            array[left] = array[right];
            array[right] = temp;
            left++;
            right--;
        }
    }
    return left;
}

quick_sort([6,1,23,4,2,3]); // [1, 2, 3, 4, 6, 23]