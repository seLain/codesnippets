import sys
from collections import Counter

def migratoryBirds(n, ar):
    # Complete this function
    b_counter = Counter(ar)
    b_common = b_counter.most_common()
    answer = b_common[0][0]
    for i in range(1, len(b_common)):
        if b_common[i][1] < b_common[i-1][1]:
            break
        if b_common[i][0] < answer:
            answer = b_common[i][0]
    return answer