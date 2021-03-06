'''
Input: an integer
Returns: an integer
'''
# runtime 0(3^n)
def eating_cookies(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return eating_cookies(n-3) + eating_cookies(n-2) + eating_cookies(n-1)

# the cache allows us to save our work
# cache is a dictionary where keys is the n, value is the answer

# RUNTIME: 0(n)
def eating_cookies(n, cache):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    # check if the answer is in our cache
    elif cache[n] > 0:
        return cache[n]
    else:
        # otherwise, our cache doesn't contain the answer, so we'll use our
        # recursive logic to calcuate it and then save the answer in our cache
        # for future uses
        cache[n] = eating_cookies(n-3, cache) + eating_cookies(n-2, cache) + eating_cookies(n-1, cache)
    return cache[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
