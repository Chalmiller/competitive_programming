function editDistanceDP(str1, str2, length1, length2) {
    var dpMatrix = [];

    for (var i = 0; i < length1 + 1; i++) {
        dpMatrix[i] = [];
        for (var j = 0; j < length2 + 1; j++) {
            dpmatrix[i][j] = undefined;
        }
    }

    for (var i = 0; i < length1 + 1; i++) {
        for (var j = 0; j < length2 + 1; j++) {
            if (i == 0) {
                dpMatrix[i][j] = j;
            } else if (j== 0) {
                dpMatrix[i][j] = i;
            } else if (str1[i - 1] == str2[j - 1]) {
                dpMatrix[i][j] = dpMatrix[i - 1][j - 1];
            } else {
                var insertCost = dpMatrix[i][j - 1],
                    removeCost = dpMatrix[i - 1][j],
                    replaceCost = dpMatrix[i - 1][j - 1];

                dpMatrix[i][j] = 1 + Math.min(insertCost, removeCost, replaceCost);
            }
        }
    }
    return dpMatrix[length1][length2];
}

function editDistanceDPWrapper(str1, str2) {
    return editDistanceDP(str1, str2, str1.length, str2.length);
}