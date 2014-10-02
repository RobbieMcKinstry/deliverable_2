import fold_math as fm

def subtract_fold(subtrahend, minuend):
    """
    Takes a numeric argument and a fold, and subtracts the sum of the fold from the numeric argument.
    """
    return subtrahend - minuend.add()

def divide_by_fold(numerator, denominator):
    """
    Takes a numeric argument and a fold, and divides the product of the fold from the argument
    """
    return numerator / denominator.multiply()

def add_reciprical(first, second):
    """
    Takes a numeric argument and a fold, and adds the inverse sum of the fold to the argument
    """
    return fm.add([ first, second.inverse_sum()])

class Fold:

    def __init__(self, elements, cores=4):
        self.elements = elements
        self.cores = cores

    # applies the multiply function to the arguments in the fold.
    def multiply(self):
        return fm.multiply(self.elements, cores=self.cores)

    # Applies the addition function to the arugments in the fold
    def add(self):
        return fm.add(self.elements, cores=self.cores)
       
    def inverse_sum(self):
        return 1/self.add()
