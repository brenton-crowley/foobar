# Most junior henchman gets exactly 1 LAMB
# A henchman will revolt if the henchman directly above them gets more than double than they do.
# A senior henchman will revolt if the combined value of the two immediate subordinates is more than theirs.
# --- Above rule doesn't apply to the two most junior henchman. 2nd most junior would require at least as many as most junior
# You can always find more henchman to pay. Must always pay another henchman.
# A single lamb cannot be divided

# return a difference between the minimum and maximum number of henchman you can share the total_lambs between.

def solution(total_lambs):
    return num_henchmen(total_lambs, 'S') - num_henchmen(total_lambs, 'G')

def num_henchmen(max_lambs, feeling="G"):
    '''
    return: the total number of henchmen
    max_lambs: is the total allowed lambs willing to be distrbuted to henchmen
    feeling: is either "G" for generous or "S" for stingy.
    '''

    lambs_count = 0
    henchmen = []

    while True:
        n = len(henchmen)
        n1 = n-1
        n2 = n-2

        if feeling.upper() not in 'SG':
            raise Exception("Invalid feeling. Must be either 'S' or 'G'")

        if feeling.upper() == "S":
            next_lambs = henchmen[n1] + henchmen[n2] if n > 1 else 1
        else:
            next_lambs = 2**(len(henchmen))

        if lambs_count + next_lambs <= max_lambs:
            henchmen.append(next_lambs)
            lambs_count += next_lambs
        else:
            break

    print(f"lambs_count: {lambs_count}")
    print(f"henchmen: {henchmen}")
    print(f"len(henchmen): {len(henchmen)}")

    return len(henchmen)
