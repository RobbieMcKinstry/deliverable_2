from multiprocessing import Pool

# average 
# multi         check
# division      check
# factorial     check
# combination
# add           check
# subtract      check

def average(arguments, cores=4):
    pass

def permutate(n, r, cores=4):
    pass

def power(base, exponent, cores=4):
    pass

def factorial(n, cores=4):
    factors = range(1, n + 1)
    return multiply(factors, cores=cores)

def combination(n, r, cores=4):
    pass
#    n! /(k! * (n-k)!)

def divide(arguments, cores=4):
    numerator = arguments[0]
    denominator = multiply(arguments[1:], cores=cores)
    return numerator/divisor        # TODO will this fail because of integer division ???

def multiply(arguments, cores=4):
    def multi_list(my_list):
        total = 1
        for argument in arguments:
            total *= argument
        return total

    return do_mapping(multi_list, arguments, cores)

def subtract(arguments, cores=4):
    minuend = arguments[0]
    subtrahend = do_mapping(sum, arguments[1:], cores)
    return minuend - subtrahend

def add(arguments, cores=4):
    return do_mapping(sum, arguments, cores=cores)



def split_fold(arguments, cores):
    """
    Cores is the number of subprocesses you intend to spawn
    arguments is the list whose elements are the values you want to compute over.
    """
    assert type(arguments) == list, 'Your first positional argument is not a list. Please pass in a list.'
    result = []
    if len(arguments) < cores:
        result.append(arguments)
        return result

    size = len(arguments)/cores # the size of each computed chunk
    for num in range(cores):
        start = num*size
        end = (num+1)*size
        result.append(arguments[start:end])

    return result


def do_mapping(function, arguments, cores):
    """
    Function is the function over which you intend to fold.
    Arguments is a list containing all of the elements in the fold
    Cores is the number of cores you want to spread this bad boy across.
    What is returned is the LIST containing each of the mapped values.
    """
    assert type(arguments) == list, 'Your first positional argument is not a list. Please pass in a list.'
    chunks = split_fold(arguments, cores)
    pool = Pool(processes=cores)
    partials = pool.map(function, chunks)
    return function(partials)


if __name__ == '__main__':
    def f(x):
        return x*x
    pool = Pool(processes=4)              # start 4 worker processes
    print pool.map(f, range(10))          # prints "[0, 1, 4,..., 81]"
