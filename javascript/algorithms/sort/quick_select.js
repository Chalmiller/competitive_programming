let array = [1,3,3,-2,3,14,7,8,1,2,2];

function quick_select_in_place(A, l, h, k) {
    let p = partition(A, l, h);
    if (p == (k-1)) {
        return A[p];
    } else if (p > (k-1)) {
        return quick_select_in_place(A, l, p - 1, k);
    } else {
        return quick_select_in_place(A, p + 1, h, k);
    }
}

function median_quick_select(array) {
    return quick_select_in_place(array, 0, array.length - 1, Math.floor(array.length/2));
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