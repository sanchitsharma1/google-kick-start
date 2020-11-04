"""
PROBLEM STATEMENT LINK --> https://codingcompetitions.withgoogle.com/kickstart/round/0000000000434944/0000000000434c05
"""

# Solution
"""
In this problem , we need to sort the list and print the number of swaps done while sorting.
Therefore, after every input (except the first one), we will compare the actual list with the sorted list, if both lists are identical, that means the actual list is sorted.
Else, a single swap will make the list sorted, so we increment the swap_counter and sort the actual list
"""

# Implementation

t = int(input())

for i in range(t):

    n = int(input())

    cards = []

    swap_counter = 0

    for _ in range(n):

        cards.append(input())

        if len(cards) > 1:

            if cards != sorted(cards):

                swap_counter += 1
                cards.sort()

    print("Case #{}: {}".format(i+1, swap_counter))
