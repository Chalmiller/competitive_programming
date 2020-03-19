function countCoinWaysDP(coinArr, numCoins, coinValue) {
    var dpMatrix = [];

    for (var i = 0; i <= coinValue; i++) {
        dpMatrix[i] = [];
        for (var j = 0; j < numCoins; j++) {
            dpMatrix[i][j] = undefined;
        }
    }

    for (var i = 0; i < numCoins; i++) {
        dpMatrix[0][i] = 1;
    }

    for (var i = 1; i < coinValue + 1; i++) {
        for (var j = 0; j < numCoins; j++) {
            var temp1 = 0, temp2 = 0;

            if (i - coinArr[j] >= 0) {
                temp1 = dpMatrix[i - coinArr[j]][j];
            }

            if (j >= 1) {
                temp2 = dpMatrix[i][j - 1];
            }

            dpMatrix[i][j] = temp1 + temp2;
        }
    }
    return dpMatrix[coinValue][numCoins - 1];
}

function countCoinwaysDPWrapper(coinArr, coinValue) {
    return cointCoinWaysDP(coinArr, coinArr.length, coinValue);
}