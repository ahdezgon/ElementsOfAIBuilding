import numpy as np

def generate(p1)
    return np.random.choice([0,1], p=[1-p1, p1], size=10000)

def count(seq):
    i = 0
    cnt = 0
    while i<len(seq)-1:
        if seq[i] and i+4<len(seq):
            ones = 1
            for j in range(1, 5):
                if seq[i+j]:
                    ones += 1
            if ones==5:
                cnt += 1
        i+=1
    return cnt

def main(p1):
    seq = generate(p1)
    return count(seq)

print(main(2/3))
