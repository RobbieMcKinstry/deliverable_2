Calculator Utilizing Multiple Cores for Arithmetic

Matt Rubel and Robbie McKinstry

CS1699 - DELIVERABLE 2: Unit Testing and Code Coverage


















Summary:
       The application being tested is a calculator that we developed using python. Each function that the calculator can perform works by taking in individual, or an array, of operands and the number of cores that the computer can utilize to make these computations. Our testing will focus on the ability of these computational functions to work with the ability to utilize a various number of cores. Our tests will also test the accuracy of the mathematical functions. The functions will then process the operands and return the result. The functions we support will be as follows:
-Addition: will take in array of operands and add them all together and return result
-Subtraction: will take in array of operands and add together the second to last values and subtract that value from the first value
-Multiplication: will take in array of operands and multiply them all together and return result
-Division: will take in array of operands and multiply together the second to last values and divide the first value by the multiplied product of the second to last values.
-Power: will take in two separate values and the method will return the result of raising the first value to the second value
-Combination: will take in two separate values and return the result of (first value)C(second value)
-Permutation: will take in two separate values and return the result of (first value)P(second value)
-Factorial: will take in a single integer and return the factorial of that integer
-Average: will take in an array of integers and return the average value of the integers in the array

We will also create an object called Fold, in which we overload the addition, subtraction, multiplication and division methods, for stub and mock testing purposes. We chose this application because it is a simple, easy to implement and understand, program and it lends itself very well to unit testing. The tests can be designed very concisely, as the use of standard math functions makes it easy to determine the expected return values for a given input.
Issues:
       When writing our tests, we came across a number of issues with how to handle input that isn’t suitable to perform calculations. As responding appropriately to input that isn’t suitable to calculation is important, we realized that we would have to carefully enforce the requirements for proper input. With this in mind, we included a number of tests, at least one for each function, that checked to ensure that the method would handle bad input by returning null.
All of our tests all passed.
Code location:
Our code can be found at www.github.com/bravenewprince/deliverable_2


