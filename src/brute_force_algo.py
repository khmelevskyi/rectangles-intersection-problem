def brute_force_algo(P):
    n = len(P)
    
    def is_valid_subset(subset):
        for i in range(n):
            for j in range(i+1, n):
                if subset[i] == 1 and subset[j] == 1 and P[i][j] == 1:
                    return False
        return True
    
    max_stripes = 0
    best_subset = None
    
    for i in range(2**n):

        binary_str = bin(i)[2:].zfill(n) # remove '0b' prefix and fill the binary with zeros
        subset = [int(bit) for bit in binary_str]
        if is_valid_subset(subset):
            num_stripes = sum(subset)
            if num_stripes > max_stripes:
                max_stripes = num_stripes
                best_subset = subset
    
    return best_subset, max_stripes

