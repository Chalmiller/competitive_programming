var cache = {};

function fiboBest(n) {
    if (n <= 1) return n;
    if (cache[n]) return cache[n];
    return (cache[n]=fiboBest(n-1)+fiboBest(n-2));
}

function waysToCoverStepsDP(step) {
    var cache = {};
    if (step < 0) return 0;
    if (step == 0) return 1;
    if (cache[step]) {
        return cache[step];
    } else {
        cache[step] = waysToCoverStepsDP(step - 1) + waysToCoverStepsDP(step - 2) + waysToCoverStepsDP(step - 3);
        return cache[step];
    }
}

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
        var current = knapsackDP(index-1, weights, values, target), currentPlusOther = values[index] + knapsackDP(index-1, weights, values, target - weights[index]);
        result = Math.max(current, currentPlusOther);
    }
    matrixDP[index + '-' + target] = result;
    return result;
}