
def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    n_apple = 0
    for apple in apples:
        if apple + a >= s and apple + a <= t:
            n_apple += 1

    n_orange = 0
    for orange in oranges:
        if orange + b >= s and orange + b <= t:
            n_orange += 1

    print(n_apple)
    print(n_orange)