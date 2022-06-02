a = [1, 2, 3]
b = [3, 2, 1]

def compareTriplets(a, b):
    a_result = 0
    b_result = 0
    for i , num in enumerate(a):
        if a[i] > b[i]:
            a_result += 1
        if a[i] < b[i]:
            b_result += 1
    return list((a_result , b_result))

print(compareTriplets(a, b))