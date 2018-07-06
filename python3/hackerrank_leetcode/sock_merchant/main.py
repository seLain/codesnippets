
def sockMerchant(n, ar):
    # Complete this function
    loosed = []
    sold = 0
    for sock in ar:
        if sock in loosed:
            loosed.remove(sock)
            sold += 1
        else:
            loosed.append(sock)
    return sold