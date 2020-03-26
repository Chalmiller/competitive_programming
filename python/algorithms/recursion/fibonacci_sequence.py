def fibonacci_sequence(n, seq):
    if n < 2:
        seq.extend([n])
        return seq
    else:
        return seq.extend([fibonacci_sequence()])