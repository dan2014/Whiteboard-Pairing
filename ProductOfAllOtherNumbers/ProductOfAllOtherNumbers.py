def findProduct(arr):
    new_arr = [None] * len(arr)
    product = 1
    for i in arr:
        product *= i
    for j,k in enumerate(arr):
        new_arr[j] = product//k
    return new_arr


def findProductNoDivision(arr):
    new_arr = [1] * len(arr)
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                continue
            else:
               new_arr[i] *= arr[j]
    return new_arr


test_arr = [1, 7, 3, 4]
# print(findProduct(test_arr))

print(findProductNoDivision(test_arr))