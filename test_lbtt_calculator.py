import unittest
from lbtt_calculator import LBTT

class TestLBTT(unittest.TestCase):
    """
    This class provides the unit tests for the LBTT calculator
    """
    
    def setUp(self):
        """
        Set up the LBTT calculator
        """
        self.lbtt_calculator = LBTT()
        
    def test_calculate_lbtt_default_scenario(self):
        """
        Test the LBTT calculator with the default tax rate values
        """
        price_list = [0, 1000, 140000, 145000, 200000, 250000, 300000, 325000, 500000, 750000, 900000, 20000000]
        expected_list = [0, 0, 0, 0, 1100, 2100, 4600, 5850, 23350, 48350, 66350, 2358350]
        for index, price in enumerate(price_list):
            with self.subTest(index=index):
                lbtt = self.lbtt_calculator.calculate(price)
                expected = expected_list[index]
                self.assertEqual(lbtt, expected)
        
    def test_calculate_lbtt_negative_price(self):
        """
        Test the LBTT calculator with a negative price
        """
        price = -250000
        with self.assertRaises(ValueError):
            self.lbtt_calculator.calculate(price)
            
    def test_calculate_lbtt_zero_price(self):
        """
        Test the LBTT calculator with a zero price
        """
        price = 0
        lbtt = self.lbtt_calculator.calculate(price)
        self.assertEqual(lbtt, 0)
    
    def test_calculate_lbtt_large_price(self):
        """
        Test the LBTT calculator with a large price
        """
        price = 10**11+1
        with self.assertRaises(ValueError):
            self.lbtt_calculator.calculate(price)
            
    def test_calculate_lbtt_decimal_price(self):
        """
        Test the LBTT calculator with a decimal price
        """
        price = 150000.34524353313131
        lbtt = self.lbtt_calculator.calculate(price)
        expected = round((round(price, 2) - 145000)*0.02, 2)
        self.assertEqual(lbtt, expected)
            
            
if __name__ == '__main__':
    unittest.main()