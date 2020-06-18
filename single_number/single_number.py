'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    for i in arr:
        if arr.count(i) == 1:
            return i

# def single_number(arr):
#     s = set()
#     for x in arr:
#         if x in s:
#             s.remove(x)
#         else:
#             s.add(x)
#     return list(s)[0]        


    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")