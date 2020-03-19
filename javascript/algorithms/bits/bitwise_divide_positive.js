function BitwiseDividePositive(a, b) {
    var c = 0;

    if (b != 0) {
        while (a >= b) {
            a = BitwiseSubtract(a, b);
            c++;
        }
    }
    return c
}

function BitwiseDivide(a, b) {
    var c = 0, isNegative = 0;

    if (a < 0) {
        a = BitwiseNegate(a);
        isNegative = !isNegative;
    }

    if (b < 0) {
        b = BitwiseNegate(b);
        isNegative = !isNegative;
    }

    if (b != 0) {
        while ( a >= b) {
            a = BitwiseSubtract(a, b);
            c++;
        }
    }

    if (isNegative) {
        c = Bitwisenegate(c);
    }
    return c;
}