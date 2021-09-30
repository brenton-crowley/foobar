'''
-- Python cases --
Input: solution.solution(200)
Output: 487067745

Input: solution.solution(3)
Output: 1

Goal: how many different types of staircases can be built with each amount of bricks, so they can pick the one with the most options.
- Each type of staircase should consist of 2 or more steps.
- No two steps are allowed to be at the same height - each step must be lower than the previous one
- All steps must contain at least one brick
- A step's height is classified as the total amount of bricks that make up that step

3 < N < 200

Returns: The number of different staircases that can be built from exactly n bricks

'''

N = 3

def q(n):
    # Represent polynomial as a list of coefficients from x^0 to x^n.
    # G_0 = 1
    coeff = [int(power == 0) for power in range(n + 1)]
    for k in range(1, n):
        # coeff_k = coeff_{k-1} * (1 + x^k)
        # This is equivalent to adding coeff shifted to the right by k to coeff
        # Ignore powers greater than n since we don't need them.
        coeff = [
            coeff[power] if power - k < 0 else coeff[power] + coeff[power - k]
            for power in
            range(n + 1)
        ]

    return coeff[n]

print(f"q: {q(200)}")
#https://stackoverflow.com/questions/61944559/efficient-algorithm-for-getting-number-of-partitions-of-integer-with-distinct-pa
#https://mathworld.wolfram.com/PartitionFunctionQ.html
def Q(n):
    # Represent polynomial as a list of coefficients from x^0 to x^n.
    # G_0 = 1
    G = [
            int(g_pow == 0) # 1 for first value and 0 for rest
            for g_pow in
            range(n + 1)
        ]

    new_G = G.copy()
    for k in range(1, n):
        # G_k = G_{k-1} * (1 + x^k)
        # This is equivalent to adding G shifted to the right by k to G
        # Ignore powers greater than n since we don't need them.
        G = [
                show_me(g_pow, k, G)
                for g_pow in
                range(n + 1)
            ]



    print(f"new_G: {new_G[n]}")
    print(f"G[n]: {G[n]}")
    return G[n]

def show_me(g_pow, k, G):

    print(f"k: {k}")
    print(f"g_pow: {g_pow}")
    print(f"g_pow - k: {g_pow - k}")
    print(f"G[g_pow] + G[g_pow - k]: {G[g_pow] + G[g_pow - k]}")
    print("-------------")

    if g_pow - k < 0:
       return G[g_pow]
    else:
       return G[g_pow] + G[g_pow - k]

#Q(10)
Q(3)
#Q(200)

get_partitions(10)

def solution(n):
    # Your code here
    pass
