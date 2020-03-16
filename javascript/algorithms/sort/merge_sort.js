function merge(leftA, rightA) {
    let results = [], leftIndex = 0, rightIndex = 0;

    while (leftIndex < leftA.length && rightIndex < rightA.length) {
        if (leftA[leftIndex] < rightA[rightIndex]) {
            results.push(leftA[leftIndex++]);
        } else {
            results.push(rightA[rightIndex++]);
        }
    }
    let leftRemains = leftA.slice(leftIndex),
        rightRemains = rightA.slice(rightIndex);

    return results.concat(leftRemains).concat(rightRemains);
}

function merge_sort(array) {
    if (array.length < 2) {
        return array;
    }

    let mid_point = Math.floor((array.length) / 2),
        leftArray = array.slice(0, mid_point),
        rightArray = array.slice(mid_point);

        return merge(merge_sort(leftArray), merge_sort(rightArray));
}

merge_sort([6,1,23,4,2,3]);