function BitwiseNegate(a) {
    return BitwiseAdd(~a, 1);
}

function BitwiseSubtract(a, b) {
    return BitwiseAdd(a, BitwiseNegate(b));
}