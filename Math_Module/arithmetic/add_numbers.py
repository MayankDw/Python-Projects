# Add function to add dynamic set of number
# passed in parameters


def add_num(*args):
    total = 0
    for i in args:
        total += i
    return total