def bitwiseAnd(N, K):
    # Write your code here
    max1 = 0
    for a in range(1,N+1):
        for b in range(1,a):
            bitw = a&b
            if max1 < bitw < K:
                max1 = bitw
                if bitw == K-1:
                    return max1
    return max1            
