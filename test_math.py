import fold_math
import unittest

class TestMathFunctions(unittest.TestCase):

    
	""" Addition function tests """
	def test_add(self):
		""" 
		This will test the functionality of the add() function. 
		The function will take in an array of integers and return
		the sum of all of the integers in the array. The test passes
		if the sum of all of the integers in the array is the returned
		value and fails otherwise.
		"""
        assert 9 == add([0,3,4,2])
	def test_neg_add(self):
		"""
		This will test the functionality of the add() function.
		The function will take in an array of integers that contain
		some negative numbers. The function should have the ability
		to add negative numbers. The test will pass if the function
		returns the sum of all positive and negative integers and
		fails otherwise.
		"""
		assert -2 == add([-2,-1,4,-3])
	def test_add_invalid_input(self):
		"""
		This will test the functionality of the add() function.
		This function will take in an array containing only one
		integer value. Since there are a minimum of two values
		needed to perform addition, the function should return
		null. If the function returns null, the test passes,
		fails otherwise.
		"""
		assert null == add([15])

	""" Subtraction function tests"""
    def test_sub(self):
		"""
		This will test the functionality of the sub() function.
		The function will take in an array of integers as parameters
		and will subtract the added value of each value in the array
		after the first value from the first value. The test passes
		if the returned value is equal to first value minus sum of
		the rest of the array values and fails otherwise.
		"""
        assert 10 == sub([20,3,6,1])
	def test_neg_sub(self):
		"""
		This will test the functionality of the sub() function.
		An array will be passed in where the values added, to be
		subtracted from the first value in the array, will add to
		a value less than zero. Meaning, the first value will be
		subtracted by a negative number. The function should be
		able to properly handle subtracting by negative numbers.
		The test will pass if the returned value is equivalent to
		the first value minus the sum of the rest of the values and
		fails otherwise."""
		assert 13 == sub([12,-3,2])
	def test_sub_invalid_input(self):
		"""
		This will test the functionality of the sub() function.
		This function will take in an array containing only one
		integer value. Since there are a minimum of two values
		needed to perform subtraction, the function should return
		null. If the function returns null, the test passes,
		fails otherwise.
		"""
		assert null == sub([15])
		
	""" Multiplication function tests"""
    def test_mult(self):
		"""
		This will test the functionality of the mult() function.
		The function will take in an array of integers and multiply 
		them together. The test passes if the returned value is the
		product of all of the values entered in the array.
		"""
        assert 72 == mult([3,2,6,2])
	def test_neg_multiplication
		"""
		This will test the functionality of the mult() function.
		The function will take in an odd number of negative
		integers and the rest positive (non-zero) integers. The
		function should return the appropriate negative integer
		and passes if it does so. The test fails otherwise.
		"""
		assert -180 == mult([-2,-3,6,-5])
	def test_mult_invalid_input(self):
		"""
		This will test the functionality of the mult() function.
		This function will take in an array containing only one
		integer value. Since there are a minimum of two values
		needed to perform multiplication, the function should return
		null. If the function returns null, the test passes,
		fails otherwise.
		"""
		assert null == mult([10])
		
	""" Division function tests """
	def test_div(self):
		"""
		This will test the functionality of the div() function.
		This function will take in an array of integers and multiply
		every value together to make the denominator except the 
		first value. The first value will constitute the numerator and
		divided by the denominator. The test will pass if the returned
		value is equal to the numerator divided by the denominator.
		"""
		assert 3 == div([24,2,4])
	def test_div_by_zero(self):
		"""
		This will test the functionality of the div() function.
		This function will take in a positive number and a zero
		in the input array. This means that the function should
		try to divide by zero, to which a solution does not exist.
		The test passes if the function returns null and fails otherwise.
		"""
		assert null == div([24,0])
	def test_div_invalid_input(self):
		"""
		This will test the functionality of the div() function.
		This function will take in an array containing only one
		integer value. Since there are a minimum of two values
		needed to perform division, the function should return
		null. If the function returns null, the test passes,
		fails otherwise.
		"""
		assert null == div([23])
	
	""" Factorial function tests """
	def test_fact(self):
		"""
		This will test the functionality of the fact() function.
		This function will take in a single integer value and 
		calculate the appropriate factorial value for that integer.
		The test will pass if the value returned is the appropriate
		factorial value for the integer passed in.
		"""
		assert 120 == fact(5)
	def test_neg_fact(self):
		"""
		This will test the functionality of the fact() function.
		This function will take in a negative integer and should
		return null since it is impossible to take the factorial
		of a negative number. The test will pass if a null value is
		returned and fail otherwise.
		"""
		assert null == fact(-3)
		
	""" Average function tests"""	
	def test_avg(self):
		"""
		This will test the functionality of the avg() function.
		This function will take in an array of integers and calculate
		the average of the included integers. The test will pass if
		the returned value is the average of the integers provided in
		the array and fail otherwise.
		"""
		assert 12 == avg([10,15,11])
	def test_null_avg(self):
		"""
		This will test the functionality of the avg() function.
		This will take in an array with 0 elements in it. The 
		function should return a null value. The test will pass if
		the returned value is null and fail otherwise
		"""
		assert null == avg([])
	
	""" Combination function tests """
	def test_comb(self):
		"""
		This will test the functionality of the comb() function.
		THis function will take in the n and r values to perform a
		combination calculation. The test will pass if the returned
		value is the appropriate combination of n and r and fail
		otherwise.
		"""
		assert 220 == comb(12,3)
	def test_neg_comb
		"""
		This will test the functionality of the comb() function.
		This function will take in a negative n value. This should
		cause the function to return a null value because n must because
		an integer >= 0 to use the mathematical function. The test will
		pass if the returned value is null and fail otherwise.
		"""
		assert null == comb(-2,4)
		
	""" Permutation function test """
	def test_perm(self):
		"""
		This will test the functionality of the perm() function.
		This function will take in the n and r values to perform a
		permutation calculation. THe test will pass if the returned
		value is the appropriate permutation of n and r and fail
		otherwise.
		"""
		assert 840 == perm(7,4)
	def test_neg_perm
		"""
		This will test the functionality of the perm() function.
		This function will take in a negative n value. This should
		cause the function to return a null value because n must because
		an integer >= 0 to use the mathematical function. The test will
		pass if the returned value is null.
		"""
		assert null == perm(-2,4)
		
	""" Power function tests """
	def test_power(self):
		"""
		This will test the functionality of the power() function.
		THis function will take in the n and e values and raise
		the n value to the e. This test will pass if the returned
		value is equivalent to n^e, otherwise it will fail.
		"""
		assert 343 == power(7,3)
	def test_negative_power
		"""
		This will test the functionality of the power() function.
		This test will ensure that the power function handles raising 
		a negative number to a power as specified. The test will
		pass if the returned value is equivalent to n^e, with e being
		a negative number, otherwise it will fail.
		"""
		assert 100 == power(-10, 2)
	

if __name__ == '__main__':
    unittest.main()