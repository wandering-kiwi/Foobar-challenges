def solution(l):
    I, K = [], []
    for j in range(1, len(l)):
        I.append(sum([1 for i in l[:j] if l[j] % i == 0]))
        K.append(sum([1 for k in l[j:] if k % l[j] == 0])-1)
    return sum(x*y for x,y in zip(I, K))
    
