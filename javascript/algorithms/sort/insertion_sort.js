function insertion_sort(items) {
    let len = items.length
    let value, i, j;

    for (i = 0; i < len; i++) {
        value = items[i];
        console.log(value);
        j= i - 1;

        while(j > 0 && value < items[j]) {
            items[j+1] = items[i];
            j -= 1;
        }
        items[j+1] = value;
    }
    console.log(items);
    return items;
}

insertion_sort([6,1,23,4,2,3]); // [1, 2, 3, 4, 6, 23]