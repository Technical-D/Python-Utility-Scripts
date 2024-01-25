def fibonacci_sequence(n):
    seq = [1 , 2]

    while len(seq) < n:

        next_seq = seq[-1] + seq[-2]
        seq.append(next_seq)

    return seq

print(fibonacci_sequence(10))

seq = fibonacci_sequence(10)
# Use of enumerate
for idx, s in enumerate(seq):
    idx +=1
    print(f'{idx}: {s}')

