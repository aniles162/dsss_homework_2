import unittest
from math_quiz import get_number, get_operator, gen_math_problem


class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = get_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        # TODO
        # Test if the operators are the correct symbols

        operators = {'+', '-', '*'}
        for _ in range(1000): # Test a large number of random values
            op = get_operator() 
            self.assertIn(op, operators) # test if one of the random chosen operators "op" is in the set of "operators"

        pass

    def test_function_C(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                
                (3, 6, '*', '3 * 6', 18),
                (7, 1, '-', '7 - 1', 6),
                (4, 8, '+', '4 + 8', 12),
                (2, 5, '*', '2 * 5', 10),
                (9, 7, '-', '9 - 7', 2)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                
                problem, answer = gen_math_problem(num1, num2, operator)
                self.assertEqual(problem, expected_problem)  
                self.assertEqual(answer, expected_answer)   
                pass

if __name__ == "__main__":
    unittest.main()
