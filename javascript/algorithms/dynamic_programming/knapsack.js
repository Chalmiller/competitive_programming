function knapsackDP(index, weights, values, target, matrixDP) {
    var result = 0;

    if (matrixDP[index + '-' + target]) {
        return matrixDP[index + '-' + target];
    }

    if (index <= -1 || target <= 0) {
        result = 0;
    } else if (weights[index] > target) {
        result = knapsackDP(index - 1, weights, values, target, matrixDP);
    } else {
        var current = knapsackDP(index - 1, weights, values, target),
            currentPlusOther = values[index] + knapsackDP(index - 1, weights, values, target - weights[index]);
        result = Math.max(current, currentPlusOther)
    }
    matrixDP[index + '-' + target] = result;
    return result;
}