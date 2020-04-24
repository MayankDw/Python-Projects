# Sub function to subtract dynamic set of number
# passed in parameters

def sub_num(*args):
    total = args[0]
    numbers = iter(args)
    next(numbers)
    for i in numbers:
            total = total - i
            
    return total