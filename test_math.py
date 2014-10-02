from fold_math import subtract, power, permutate, combination, add, factorial, multiply, divide, average, split_fold
import unittest
import fold

class MockFold:

    def __init__(self, elements, cores=4):
        self.elements = elements

    def multiply(self):
        self.called_multiply = True
        return 1

    def add(self):
        self.called_add = True
        return 1



class TestFoldClass(unittest.TestCase):
    """
    Tests the functions and the class in fold.py
    """

    def test_subtract_fold(self):
        f = MockFold([1, 2, 3, 4])
        fold.subtract_fold(1, f)
        assert f.called_add

    def test_divide_by_fold(self):
        f = MockFold([1, 2, 3, 4])
        fold.divide_by_fold(1, f)
        assert f.called_multiply


class TestMathFunctions(unittest.TestCase):
    """
    Tests for the utility functions found in fold_math
    """

    def test_when_cores_are_few(self):
        """
        This function tests the split_fold() function to see how it returns the arguments list when the number of elements its accepting is more than the number of cores.
        """
        arguments = [1]
        expected = [[1]]
        observed = split_fold(arguments, cores=1)
        assert expected == observed, 'Expected: {0}\nObserved: {1}'.format(expected, observed)
       
        arguments = [1, 1]
        expected = [[1, 1]]
        observed = split_fold(arguments, cores=1)
        assert expected == observed, 'Expected: {0}\nObserved: {1}'.format(expected, observed)

    def test_when_cores_are_many(self):
        """
        This function tests the split_fold() function to see how it handles when the argument list has less elements than the number of cores available.
        """
        arguments = [1]
        expected = [[1]]
        observed = split_fold(arguments, cores=4)
        assert expected == observed, 'Expected: {0}\nObserved: {1}'.format(expected, observed)


    """ Addition function tests """
    def test_when_add_has_no_edge_cases(self):
        """ 
        This will test the functionality of the add() function. 
        The function will take in an array of integers and return
        the sum of all of the integers in the array. The test passes
        if the sum of all of the integers in the array is the returned
        value and fails otherwise.
        """
        assert 9    == add([0, 3, 4, 2]),   'Produced an incorrect sum: expecting {0} and received {1}'.format(9, [0, 3, 4, 2,])
        assert 0    == add([0, 0, 0]),      'Produced an incorrect sum: expecting {0} and received {1}'.format(0, add([0, 0, 0]))
        assert 11   == add([10, 1]),        'Produced an incorrect sum: expecting {0} and received {1}'.format(11, add([10, 1]))
  

    def test_when_add_gets_negative_nums(self):
        """
        This will test the functionality of the add() function.
        The function will take in an array of integers that contain
        some negative numbers. The function should have the ability
        to add negative numbers. The test will pass if the function
        returns the sum of all positive and negative integers and
        fails otherwise.
        """
        result1      = add([-2, -1, 4, 3])
        result2      = add([-10, -1, -1, 5])

        assert 4     == result1, 'Expected: {0}\nObserved: {1}'.format(-2, result1)
        assert -7    == result2, 'Expected: {0}\nObserved: {1}'.format(-2, result2)
        
    
    def test_add_invalid_input(self):
        """
        This will test the functionality of the add() function.
        This function will take in an array containing only one
        integer value. Since there are a minimum of two values
        needed to perform addition, the function should return
        None. If the function returns None, the test passes,
        fails otherwise.
        """
        assert None == add([15])
        assert None == add([ 1, {} ])


    """ Subtraction function tests"""
    def test_subtraction(self):
        """
        This will test the functionality of the subtract() function.
        The function will take in an array of integers as parameters
        and will subtract the added value of each value in the array
        after the first value from the first value. The test passes
        if the returned value is equal to first value minus sum of
        the rest of the array values and fails otherwise.
        """
        assert 10 == subtract([20,3,6,1])


    def test_neg_subtraction(self):
        """
        This will test the functionality of the subtract() function.
        An array will be passed in where the values added, to be
        subtracted from the first value in the array, will add to
        a value less than zero. Meaning, the first value will be
        subtracted by a negative number. The function should be
        able to properly handle subtracting by negative numbers.
        The test will pass if the returned value is equivalent to
        the first value minus the sum of the rest of the values and
        fails otherwise."""
        assert 13 == subtract([12,-3,2])
        assert -1 == subtract([4, 5])


    def test_subtraction_invalid_input(self):
        """
        This will test the functionality of the subtract() function.
        This function will take in an array containing only one
        integer value. Since there are a minimum of two values
        needed to perform subtraction, the function should return
        None. If the function returns None, the test passes,
        fails otherwise.
        """
        assert None == subtract([15])
        assert None == subtract([10, 9, 'Hello World' ])
        assert None == subtract([100, 99, {} ])


    """ Multiplication function tests"""
    def test_multiply(self):
        """
        This will test the functionality of the multiply() function.
        The function will take in an array of integers and multiply 
        them together. The test passes if the returned value is the
        product of all of the values entered in the array.
        """
        expected = 72
        observed = multiply([3, 2, 6, 2])
        error    = 'Expected: {0}\nObserved: {1}'.format(expected, observed)
        assert expected == observed, error

        expected = 120
        observed = multiply([1, 2, 3, 4, 5])
        error    = 'Expected: {0}\nObserved: {1}'.format(expected, observed) 
        assert expected == observed, error
        

    def test_neg_multiplication(self):
	    """
	    This will test the functionality of the multiply() function.
	    The function will take in an odd number of negative
	    integers and the rest positive (non-zero) integers. The
	    function should return the appropriate negative integer
	    and passes if it does so. The test fails otherwise.
	    """
	    assert -180 == multiply([-2,-3,6,-5])


    def test_multiply_invalid_input(self):
        """
        This will test the functionality of the multiply() function.
        This function will take in an array containing only one
        integer value. Since there are a minimum of two values
        needed to perform multiplication, the function should return
        None. If the function returns None, the test passes,
        fails otherwise.
        """
        assert None == multiply([10])
		
    """ Division function tests """


    def test_divide(self):
        """
        This will test the functionality of the divide() function.
        This function will take in an array of integers and multiply
        every value together to make the denominator except the 
        first value. The first value will constitute the numerator and
        divided by the denominator. The test will pass if the returned
        value is equal to the numerator divided by the denominator.
        """
        assert 3 == divide([24,2,4])


    def test_divide_by_zero(self):
        """
        This will test the functionality of the divide() function.
        This function will take in a positive number and a zero
        in the input array. This means that the function should
        try to divide by zero, to which a solution does not exist.
        The test passes if the function returns None and fails otherwise.
        """
        assert None == divide([24,0])


    def test_divide_invalid_input(self):
        """
        This will test the functionality of the divide() function.
        This function will take in an array containing only one
        integer value. Since there are a minimum of two values
        needed to perform division, the function should return
        None. If the function returns None, the test passes,
        fails otherwise.
        """
        assert None == divide([23])
	
    """ Factorial function tests """
    def test_factorial(self):
        """
        This will test the functionality of the factorial() function.
        This function will take in a single integer value and 
        calculate the appropriate factorial value for that integer.
        The test will pass if the value returned is the appropriate
        factorial value for the integer passed in.
        """
        expected = 120
        observed = factorial(5)
        assert expected == observed, 'Expected: {0}\nObserved: {1}'.format(expected, observed)


    def test_neg_factorial(self):
        """
        This will test the functionality of the factorial() function.
        This function will take in a negative integer and should
        return None since it is impossible to take the factorial
        of a negative number. The test will pass if a None value is
        returned and fail otherwise.
        """
        assert None == factorial(-3)
		
    
    def test_average(self):
        """
        This will test the functionality of the average() function.
        This function will take in an array of integers and calculate
        the average of the included integers. The test will pass if
        the returned value is the average of the integers provided in
        the array and fail otherwise.
        """
        result = average([10, 15, 11])
        assert 12 == result, 'Expected: {0}\nObserved: {1}'.format(12, result)
    
    def test_average_has_no_args(self):
        """
        This will test the functionality of the average() function.
        This will take in an array with 0 elements in it. The 
        function should return a None value. The test will pass if
        the returned value is None and fail otherwise
        """
        assert None == average([])
	
    """ Combination function tests """ 
    def test_combination(self):
        """
        This will test the functionality of the combination() function.
        THis function will take in the n and r values to perform a
        combination calculation. The test will pass if the returned
        value is the appropriate combination of n and r and fail
        otherwise.
        """
        assert 220 == combination(12,3)
	
    def test_neg_combination(self):
        """
        This will test the functionality of the combination() function.
        This function will take in a negative n value. This should
        cause the function to return a None value because n must because
        an integer >= 0 to use the mathematical function. The test will
        pass if the returned value is None and fail otherwise.
        """
        assert None == combination(-2,4)
		
    """ Permutation function test """
    def test_permutate(self):
        """
        This will test the functionality of the permutate() function.
        This function will take in the n and r values to perform a
        permutation calculation. THe test will pass if the returned
        value is the appropriate permutation of n and r and fail
        otherwise.
        """
        assert 840 == permutate(7,4)


    def test_neg_permutate(self):
        """
        This will test the functionality of the permutate() function.
        This function will take in a negative n value. This should
        cause the function to return a None value because n must because
        an integer >= 0 to use the mathematical function. The test will
        pass if the returned value is None.
        """
        assert None == permutate(-2,4)
		
    """ Power function tests """ 
    def test_power(self):
        """
        This will test the functionality of the power() function.
        This function will take in the n and e values and raise
        the n value to the e. This test will pass if the returned
        value is equivalent to n^e, otherwise it will fail.
        """
        assert 343 == power(7,3)

    def test_when_power_is_zero(self):
        """
        This function tests when the power is zero in the power() function.
        This should always return 1, even if the base is zero (in mathematics, zero to the zero is undefinted. But we're not in mathematics, are we?
        """
        assert 1 == power(7, 0)


    def test_when_power_has_negative_base(self):
        """
        This will test the functionality of the power() function.
        This test will ensure that the power function handles raising 
        a negative number to a power as specified. The test will
        pass if the returned value is equivalent to n^e, with e being
        a negative number, otherwise it will fail.
        """
        assert 100 == power(-10, 2)
	

    def test_when_power_is_negative(self):
        """
        This function tests when the power() function has an exponent that's negative.
        """
        assert (1/4) == power(4, -1)


if __name__ == '__main__':
    unittest.main()
