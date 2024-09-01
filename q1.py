import math

def find_pairs(product):
    pairs = []
    # Iterate from 1 to the square root of the product
    for i in range(1, math.isqrt(product) + 1):
        if product % i == 0:  
            pairs.append([i, product // i])
    return pairs

# Product to find pairs for
product = 1947
pairs = find_pairs(product)
print(pairs)
