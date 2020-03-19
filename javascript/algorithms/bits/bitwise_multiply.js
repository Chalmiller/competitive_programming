function BitwiseMultiply(a, b) {
    var m = 1, c = 0;

    if (a < 0) {
        a = BitwiseNegate(a);
        b = BitwiseNegate(b);
    }
    while ( a >= m && b) {
        if (a & m) {
            c = BitwiseAdd(b, c);
        }
        b = b << 1;
        m = m << 1;
    }
    return c;
}