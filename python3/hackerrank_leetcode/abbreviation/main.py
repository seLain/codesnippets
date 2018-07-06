import sys, string

def abbreviation(a, b):
    # Complete this function

    for i in range(0, len(a)):
        # detect sudden death uppercase chars
        if a[i] in string.ascii_uppercase and a[i] not in b:
            return 'NO'
        # check if there is fit by Uppercase
        if a[i] == b[0]: # uppercase fit found
            # check the throw away part
            for c in a[0:i]:
                if c in string.ascii_uppercase:
                    return 'NO'
            # check if b running out
            if len(b) == 1:
                # check the remaining part of a
                for c in a[i+1:]:
                    if c in string.ascii_uppercase:
                        return 'NO'
                return 'YES'
            else:
                # keep check the remaining part
                return abbreviation(a[i+1:], b[1:])
        # check if there is fit by lowercase
        if a[i] == b[0].lower():
            # check the throw away part
            for c in a[0:i]:
                if c in string.ascii_uppercase:
                    return 'NO'
            # check if b running out
            if len(b) == 1:
                # check the remaining part of a
                for c in a[i+1:]:
                    if c in string.ascii_uppercase:
                        return 'NO'
                return 'YES'
            else:
                # keep check the remaining part
                return abbreviation(a[i+1:], b[1:])
    return 'NO'

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        a = input().strip()
        b = input().strip()
        result = abbreviation(a, b)
        print(result)