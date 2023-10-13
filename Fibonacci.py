def fibonacci_sequence(n):
    seq = [1 , 2]

    while len(seq) < n:

        next_seq = seq[-1] + seq[-2]
        seq.append(next_seq)

    return seq

print(fibonacci_sequence(10))